import torch
from transformers import AutoTokenizer
import numpy as np
import onnxruntime as ort
import os
import os.path
#TODO: https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/Huggingface_QuickStart.md
def get_seed():
    seed = os.getenv("RANDOM_SEED")
    return int(seed) if seed is not None else 0

torch.random.manual_seed(get_seed())

model_path = os.path.join(os.path.dirname(__file__), 'Phi-3.5-mini-instruct-onnx', 'cpu_and_mobile', 'cpu-int4-awq-block-128-acc-level-4')
onxx_model_path = os.path.join(os.path.dirname(__file__), 'Phi-3.5-mini-instruct-onnx', 'cpu_and_mobile', 'cpu-int4-awq-block-128-acc-level-4', 'phi-3.5-mini-instruct-cpu-int4-awq-block-128-acc-level-4.onnx')

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Encode input text
input_text = "why should I learn physics?"
inputs = tokenizer(input_text, return_tensors="np")

# Convert input_ids and attention_mask to int64
input_ids = inputs["input_ids"].astype(np.int64)
attention_mask = inputs["attention_mask"].astype(np.int64)

# Update `num_heads` and `head_dim` based on model requirements
num_layers = 32  # Adjust based on your model's architecture
batch_size = input_ids.shape[0]
num_heads = 32  # Adjust based on model requirements
sequence_length = input_ids.shape[1]
head_dim = 96  # Adjust based on model requirements

# Initialize past_key_values as a list of arrays to avoid dictionary overhead
past_key_values = [
    {
        'key': np.zeros((batch_size, num_heads, sequence_length, head_dim), dtype=np.float32),
        'value': np.zeros((batch_size, num_heads, sequence_length, head_dim), dtype=np.float32)
    }
    for _ in range(num_layers)
]

# Combine inputs and past_key_values
input_feed = {
    'input_ids': input_ids,
    'attention_mask': attention_mask,
    **{f'past_key_values.{i}.{k}': past_key_values[i][k] for i in range(num_layers) for k in ['key', 'value']}
}

# Load the ONNX model once to reuse during generation
session = ort.InferenceSession(onxx_model_path)

# Generate text iteratively
max_length = 150  # Adjust the maximum length of the generated text
generated_ids = input_ids

for _ in range(max_length):
    # Run inference
    outputs = session.run(None, input_feed)

    # Extract logits and updated past_key_values
    logits = outputs[0]
    present = outputs[1:]

    # Update past_key_values in place to avoid reallocation
    for i in range(num_layers):
        if past_key_values[i]['key'].shape != present[2 * i].shape:
            past_key_values[i]['key'] = np.zeros_like(present[2 * i])
        if past_key_values[i]['value'].shape != present[2 * i + 1].shape:
            past_key_values[i]['value'] = np.zeros_like(present[2 * i + 1])
        
        np.copyto(past_key_values[i]['key'], present[2 * i])
        np.copyto(past_key_values[i]['value'], present[2 * i + 1])

    # Get the next token using top-k sampling to introduce variability
    top_k = 10
    next_token_logits = logits[:, -1, :]
    top_k_indices = np.argpartition(next_token_logits, -top_k, axis=-1)[:, -top_k:]
    next_token_probs = np.take_along_axis(next_token_logits, top_k_indices, axis=-1)
    next_token_probs = np.exp(next_token_probs) / np.sum(np.exp(next_token_probs), axis=-1, keepdims=True)
    next_token_id = np.array([np.random.choice(top_k_indices[i], p=next_token_probs[i]) for i in range(batch_size)])
    
    generated_ids = np.concatenate([generated_ids, next_token_id[:, None]], axis=-1)

    # Update attention_mask to reflect attention only on the generated parts
    attention_mask = np.concatenate([attention_mask, np.ones((batch_size, 1), dtype=np.int64)], axis=-1)

    # Update input_feed with the new token and past_key_values
    input_feed = {
        'input_ids': generated_ids,
        'attention_mask': attention_mask,
        **{f'past_key_values.{i}.{k}': past_key_values[i][k] for i in range(num_layers) for k in ['key', 'value']}
    }

    # Stop if the end-of-sequence token is generated
    # Stop if the end-of-sequence token is generated, allowing more complete output
    if next_token_id[0] == tokenizer.eos_token_id and generated_ids.shape[1] > 20:
        break

# Decode the generated text
generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=False)

# Print the generated text
print(generated_text)
