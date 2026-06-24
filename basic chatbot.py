def get_bot_response(user_input):

    user_input = user_input.lower().strip()

    
    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."


def start_chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit the chat.")

    
    while True:
        
        user_message = input("You: ")

        # Check for the exit condition first
        if user_message.lower().strip() in ["bye", "goodbye"]:
            print("🤖 Chatbot: Goodbye!")
            break  

        
        response = get_bot_response(user_message)
        print(f"🤖 Chatbot: {response}")


    start_chatbot()