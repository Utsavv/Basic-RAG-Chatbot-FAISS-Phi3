# Azure AI Studio Example

This project demonstrates how to use Azure AI Studio to interact with Phi 3.5 models, generate embeddings using FAISS, and manage environment setup using PowerShell scripts.

## Project Structure

- `Azure_AI_Studio.py`: This script contains the main logic to interact with the Azure OpenAI API. It includes functions to send queries to the API and handle responses.
- `Vector_DB_Through_FAISS.py`: This script demonstrates how to use FAISS to create a vector database from text embeddings generated using the Sentence Transformers library.
- `Azure-AI-Studio-Setup.ps1`: A PowerShell script to set up the Conda environment and install necessary dependencies for the project.
- `.gitignore`: A file specifying which files and directories should be ignored by Git.
- `Documentation.txt`: A sample text file used in the `Vector_DB_Through_FAISS.py` script to generate embeddings.
- `.vscode/launch.json`: Configuration file for Visual Studio Code to set up debugging and environment variables.

## Setup Instructions

### Prerequisites

- Python 3.12
- Conda
- Visual Studio Code (optional, for debugging)

### Step 1: Set Up Conda Environment

Run the following PowerShell script to set up the Conda environment and install dependencies:

```powershell
.\Azure-AI-Studio-Setup.ps1