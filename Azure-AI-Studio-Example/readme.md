# Azure AI Studio Example

This project demonstrates how to use Azure AI Studio to interact with Phi 3.5 models, generate embeddings using FAISS, and manage environment setup using PowerShell scripts.

## Project Structure
- `Azure-AI-Studio-Setup.ps1`: This script will first create a Conda environment and then proceed to install the required dependencies. Please note that while FAISS is available exclusively through Conda, the remaining dependencies can be installed via PIP.
- `Azure_AI_Studio.py`: This script contains the main logic to interact with the Azure OpenAI API. It includes functions to send queries to the API and handle responses after authentication.
- `Vector_DB_Through_FAISS.py`: This script demonstrates how to use FAISS to create a vector database from text embeddings generated using the Sentence Transformers library. Once embeddings are created, it will use FAISS for returning top 3 matches.

- `Documentation.txt`: A sample text file used in the `Vector_DB_Through_FAISS.py` script to generate embeddings. This documentation is based on SAP rule engine documenntation publicly available

- `ChatBot.py`: This is where everything comes together. The ChatBot.py file implements a conversational chatbot by encapsulating key functionality within a ChatBot class, which handles user input processing, response generation, and output formatting. At a high level, the script begins by importing necessary NLP and machine learning libraries, configuring any constants or API keys, and initializing the ChatBot class. The chatbot class constructor loads required models or connects to external APIs for generating responses. When a user input is received, it goes through the process_input method, which standardizes and prepares the text for model inference by performing tasks like lowercasing and tokenization. The cleaned input is then passed to generate_response, which either calls an external API or uses a locally hosted model to generate a relevant reply. The respond method wraps this entire workflow, taking raw user input, invoking processing and response generation, and returning a formatted output. If run directly, ChatBot.py includes an interactive loop that allows users to engage in continuous conversation until they choose to exit.

## Setup Instructions

### Prerequisites

- Python 3.12
- Conda
- Visual Studio Code (optional, for debugging)

### Step 1: Set Up Conda Environment

Run the following PowerShell script to set up the Conda environment and install dependencies:

```powershell
.\Azure-AI-Studio-Setup.ps1
```

## TO DO: 
Fine tune model so that output is returned from a concise model then from a generic model.