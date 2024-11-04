## Step 1: Set up Conda Environment and Install Dependencies

# Create a new Conda environment and install the required libraries by running 
# the following commands in your terminal. 
# FAISS setup instructions are available at 
# https://github.com/facebookresearch/faiss/blob/main/INSTALL.md 
# Please pay attention to GPU setup. 
# If you have CPU only then execute CPU only command. 
# Perforamnce of CPU only setup will not be as good as GPU setup.

# Define the environment name
$envName = "BasicRAGChatBotPhi"
# Define the environment variables
$apiKey = "YOUR_API_KEY"
$endpoint = "https://resource-Project.location.models.ai.azure.com"

#In case if you want to delete env
#conda deactivate
#conda env remove --name BasicRAGChatBotPhi
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
# Halt execution for 30 seconds so that env can be activated properly
Write-Output "Pausing for 30 seconds..."
Start-Sleep -Seconds 30

if ($env:CONDA_DEFAULT_ENV) {
    Write-Output "Conda environment '$env:CONDA_DEFAULT_ENV' is activated."
} else {
    Write-Output "No Conda environment is activated."
}

# Check if the current environment name matches $envName
$currentEnv = $env:CONDA_DEFAULT_ENV

if ($currentEnv -ne $envName) {
    Write-Output "Current environment '$currentEnv' does not match the required environment '$envName'. Exiting..."
    exit 1
}

# CPU-only version

pip install openai
pip install transformers
pip install python-dotenv
pip install azure-ai-inference

# Set the environment variables
#You can create 