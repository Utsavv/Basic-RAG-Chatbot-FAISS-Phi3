# pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables from a .env file
#load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY")  # Use environment variable for security
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  # Use environment variable for security
# API_KEY = "ofJyD5hLMkSwXRsd6mxluP3heajkJOZY"
# ENDPOINT = "https://LLMUseCase-ChatBot.swedencentral.models.ai.azure.com"
#DEPLOYMENT_NAME = "LLMUseCase-ChatBot" #not the model name, but deployment name
# Define the headers for Azure authentication
client = ChatCompletionsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(API_KEY)
)


def send_query_to_azure(query: str):
    try:
        payload = {
        "messages": [
            {
            "role": "user",
            "content": "Please summarize following "+query
            }
        ],
        "max_tokens": 2048,
        "temperature": 0.8,
        "top_p": 0.1,
        "presence_penalty": 0,
        "frequency_penalty": 0
        }
        response = client.complete(payload)

        # Extracting response text
        result_text = response.choices[0].message.content.strip()
        return result_text
    
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    # Define your prompt
    user_query = "What is the capital of France?"

    # Send the query and get the response
    response = send_query_to_azure(user_query)
    print(f"Response from Azure AI Studio: {response}")
