import random

# Variables
greetings = ["Hello", "Hi", "How are you", "Greeting"]
chat_invitations = ["What do you want to talk about?", "You wanna talk?", "What about a small chat?", "Let's talk!"]
responses = ["You are right", "Yes", "I agree"]

jokes = {"bird": "birds are living in the Ocean",
         "fish": "fishes are living on trees",
         "human": "humans are always jumping",
         "animal": "every animal can speak English"
         }


chatbot_name = "Mia"
chatbot_prefix = chatbot_name + ": "

print(chatbot_prefix + random.choice(greetings) + "! " + "What's you name? ")
user_name = input("User: ")

user_prefix = user_name + ": "

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
            if user_replica.find(key_word) != -1:
                print(chatbot_phrase(jokes[key_word]))
                was_kidding = True
                break

        if was_kidding == False:
            print(chatbot_phrase(random.choice(responses) + ", " + user_name + ", " + user_replica))

        chat()


#Main
chat() # YOUR PROGRAM STARTS RUNNING FROM HERE!