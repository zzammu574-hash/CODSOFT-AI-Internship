def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user or "hi" in user:
            print("Chatbot: Hi there!")
        elif "how are you" in user:
            print("Chatbot: I'm doing great!")
        else:
            print("Chatbot: I don't understand.")

chatbot()