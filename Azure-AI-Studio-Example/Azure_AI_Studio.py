# pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from threading import Lock

API_KEY = os.getenv('AZURE_OPENAI_API_KEY')  # Use environment variable for security
ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')  # Use environment variable for security

if not API_KEY or not ENDPOINT:
    print("Error: API_KEY and ENDPOINT must be set in environment variables.")
    exit(1)

class AzureClientSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(AzureClientSingleton, cls).__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.client = ChatCompletionsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(API_KEY)
        )

    def get_client(self):
        return self.client

def send_query_to_azure(query: str):
    try:
        # Get the singleton client instance
        client = AzureClientSingleton().get_client()

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "Please summarize following :" + query
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
