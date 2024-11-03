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
y
pip install openai
pip install transformers
pip install python-dotenv

# Set the environment variables
[System.Environment]::SetEnvironmentVariable("AZURE_OPENAI_API_KEY", $apiKey, [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("AZURE_OPENAI_ENDPOINT", $endpoint, [System.EnvironmentVariableTarget]::User)

# Verify that the environment variables are set
Write-Output "AZURE_OPENAI_API_KEY is set to: $([System.Environment]::GetEnvironmentVariable('AZURE_OPENAI_API_KEY', [System.EnvironmentVariableTarget]::User))"
Write-Output "AZURE_OPENAI_ENDPOINT is set to: $([System.Environment]::GetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', [System.EnvironmentVariableTarget]::User))"