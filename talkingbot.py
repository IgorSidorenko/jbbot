import random

# Variables
greetings = ["Hello", "Hi", "How are you", "Greeting"]
chat_invitations = ["What do you want to talk about?", "You wanna talk?", "What about a small chat?", "Let's talk!"]
responses = ["You are right", "Yes", "I agree"]

jokes = {
    "bird": "birds are living in the Ocean",
    "fish": "fishes are living on trees",
    "human": "humans are always jumping",
    "animal": "every animal can speak English"
}

chatbot_name = "Mia"
chatbot_prefix = chatbot_name + ": "

# Functions
def chatbot_phrase(phrase):
    return chatbot_prefix + phrase

def user_phrase():
    return input(user_prefix)

def chat():
    print(chatbot_phrase(random.choice(chat_invitations)))
    user_replica = user_phrase()

    if user_replica == "Bye":
        return
    else:
        was_kidding = False
        for key_word in jokes.keys():
            if key_word in user_replica:
                print(chatbot_phrase(jokes[key_word]))
                was_kidding = True
                break

        if not was_kidding:
            print(chatbot_phrase(f"{random.choice(responses)}, {user_name}, {user_replica}"))
        chat()

def main():
    print(chatbot_phrase(random.choice(greetings)) + "! What's your name?")
    global user_name, user_prefix
    user_name = input("User: ")
    user_prefix = user_name + ": "
    chat()

if __name__ == "__main__":
    main()