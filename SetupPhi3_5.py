import onnxruntime as ort
from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct-onnx")

# Load the ONNX model
# session = ort.InferenceSession("path_to_model/phi-3.5-mini-instruct-onnx.onnx")

# # Define the input text
# input_text = "What is the golden ratio?"

# # Tokenize the input
# inputs = tokenizer(input_text, return_tensors="np")

# # Run inference
# outputs = session.run(None, {"input_ids": inputs["input_ids"]})

# # Decode the output
# output_text = tokenizer.decode(outputs[0][0], skip_special_tokens=True)
conda deactivate

# print(output_text)
