## Step 1: Set up Conda Environment and Install Dependencies

# Create a new Conda environment and install the required libraries by running 
# the following commands in your terminal. 
# FAISS setup instructions are available at 
# https://github.com/facebookresearch/faiss/blob/main/INSTALL.md 
# Please pay attention to GPU setup. 
# If you have CPU only then execute CPU only command. 
# Perforamnce of CPU only setup will not be as good as GPU setup.

# Define the environment name
$envName = "BasicRAGChatBot"

#In case if you want to delete env
#conda deactivate
#conda env remove --name BasicRAGChatBot
# Check if the environment already exists
$envExists = conda info --envs | Select-String $envName

if ($envExists) {
    Write-Output "Environment '$envName' already exists."
} else {
    Write-Output "Creating environment '$envName'..."
    conda create -n $envName python=3.12 -y
}

# Activate the environment
conda activate $envName


# CPU-only version
conda install -c pytorch faiss-cpu=1.9.0

# GPU(+CPU) version
# conda install -c pytorch -c nvidia faiss-gpu=1.9.0

# GPU(+CPU) version with NVIDIA RAFT

#Install dependencies required for Tunning Phi 3.5
# Install ONNX Runtime, FastAPI, and Uvicorn
pip install onnxruntime
conda install -c conda-forge fastapi uvicorn

# Install Faiss (CPU version), Flask, Transformers, and Torch (PyTorch)
conda install -c conda-forge faiss-cpu flask transformers pytorch

# Install Hugging Face Tokenizers
git lfs install
git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx