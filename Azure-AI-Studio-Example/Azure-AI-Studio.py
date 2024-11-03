import os
from openai import AzureOpenAI
#reference - https://github.com/Azure-Samples/openai/blob/main/Basic_Samples/Completions/basic_completions_example_sdk.ipynb
# Set up your credentials here
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# API_KEY = os.environ["AZURE_OPENAI_API_KEY"]  # Use environment variable for security
# ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]  # Use environment variable for security
API_KEY = "ofJyD5hLMkSwXRsd6mxluP3heajkJOZY"
ENDPOINT = "https://LLMUseCase-ChatBot.swedencentral.models.ai.azure.com"
DEPLOYMENT_NAME = "LLMUseCase-ChatBot" #not the model name, but deployment name

# Initialize the AzureOpenAI client with Azure-specific settings
client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=ENDPOINT,  # Use 'base_url' instead of 'api_base'
    api_version="2024-11-04"  # Ensure this matches your Azure OpenAI API version
)

def send_query_to_azure(prompt: str):
    try:
        # Call the Azure OpenAI API using the client
        response = client.completions.create(
            model=DEPLOYMENT_NAME,  # Use your model deployment name
            prompt=prompt,
            max_tokens=20
        )

        # Extracting response text
        result_text = response.choices[0].text.strip()
        return result_text
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    # Define your prompt
    user_query = "What is the capital of France?"

    # Send the query and get the response
    response = send_query_to_azure(user_query)
    print(f"Response from Azure AI Studio: {response}")
