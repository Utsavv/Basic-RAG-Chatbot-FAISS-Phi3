import onnxruntime as ort
from transformers import AutoTokenizer

# Load the tokenizer from a local directory
tokenizer = AutoTokenizer.from_pretrained(r".\Phi-3.5-mini-instruct-onnx\cpu_and_mobile\cpu-int4-awq-block-128-acc-level-4")

# Load the ONNX model
session = ort.InferenceSession(r".\Phi-3.5-mini-instruct-onnx\cpu_and_mobile\cpu-int4-awq-block-128-acc-level-4\phi-3.5-mini-instruct-cpu-int4-awq-block-128-acc-level-4.onnx")

# Define the input text
input_text = "What is the golden ratio?"

# Tokenize the input
inputs = tokenizer(input_text, return_tensors="np")

# Prepare the inputs for the model
input_feed = {
    "input_ids": inputs["input_ids"],
    "attention_mask": inputs["attention_mask"]
}

# Run inference
outputs = session.run(None, input_feed)

# Decode the output
output_text = tokenizer.decode(outputs[0][0], skip_special_tokens=True)

print(output_text)
