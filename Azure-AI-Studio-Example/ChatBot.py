from Azure_AI_Studio import send_query_to_azure
from Vector_DB_Through_FAISS import search_faiss_index

while True:
    # Prompt user for input
    user_query = input("Please enter your search query from documentation txt file (or type 'quit' to exit): ")
    
    # Check if user wants to quit
    if user_query.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break

    # Search FAISS index with user query
    faiss_result = search_faiss_index(user_query)

    # Send the FAISS result to Azure and get the response
    response = send_query_to_azure(faiss_result)
    print(f"Chatbot Response:\n\n\t\t {response}\n\n")
