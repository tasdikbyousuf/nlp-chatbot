import random
import spacy
import datetime

# Load the English language model provided by spaCy
nlp = spacy.load("en_core_web_sm")

class Chatbot:
    def __init__(self):
        # Initialize an empty memory dictionary to store information
        self.memory = {}
        # Initialize an empty user_name
        self.user_name = ""

    # Method to greet the user
    def greet(self, name):
        responses = [f"Hello {name}!", f"Hi {name}!", f"Hey {name}!", f"Greetings {name}!"]
        return random.choice(responses)

    # Method to bid farewell to the user
    def farewell(self, name):
        responses = [f"Goodbye {name}!", f"See you later {name}!", f"Bye {name}!", f"Take care {name}!"]
        return random.choice(responses)

    # Method to perform sentiment analysis on input text
    def sentiment_analysis(self, text):
        doc = nlp(text)
        sentiment_score = doc.sentiment
        if sentiment_score >= 0.5:
            return "That sounds positive!"
        elif sentiment_score <= -0.5:
            return "That sounds negative."
        else:
            return "I'm not sure about the sentiment."

    # Method to recognize named entities in input text
    def named_entity_recognition(self, text):
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    # Method to remember information provided by the user
    def remember(self, key, value):
        self.memory[key] = value

    # Method to recall stored information
    def recall(self, key):
        return self.memory.get(key, "I don't remember anything about that.")

    # Method to forget all stored information
    def forget(self):
        self.memory = {}
        self.user_name = ""

    # Method to get the current time
    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M")

    # Method to initiate the chat with the user
    def chat(self):
        self.user_name = input("What's your name? ")
        use_custom_name = input("Would you like to give the chatbot a custom name? (yes/no): ").lower()
        if use_custom_name == "yes":
            custom_name = input("What custom name would you like to use? ")
        else:
            custom_name = "Chatbot"
        print(f"Hello {self.user_name}! I'm {custom_name}. How can I assist you?")
        while True:
            user_input = input(f"{self.user_name}: ").lower()
            if user_input in ["goodbye", "exit"]:
                print(self.farewell(self.user_name))
                break
            elif user_input == "what can you do":
                print(f"{custom_name}: I can respond to greetings, farewells, perform sentiment analysis, and named entity recognition. I can also remember things. I can tell you the current time. Feel free to ask me anything!")
            elif "how are you" in user_input:
                print(f"{custom_name}: I'm just a chatbot, I don't have feelings, but thanks for asking!")
            elif "sentiment" in user_input:
                print(f"{custom_name}: {self.sentiment_analysis(user_input)}")
            elif "entities" in user_input:
                print(f"{custom_name}: Named entities in the input are: {self.named_entity_recognition(user_input)}")
            elif "remember" in user_input:
                parts = user_input.split("remember ")[1].split(" as ")
                if len(parts) == 2:
                    key, value = map(str.strip, parts)
                    self.remember(key, value)
                    print(f"{custom_name}: Okay, I'll remember that.")
                else:
                    print(f"{custom_name}: Sorry, I couldn't understand the input. Please use the format 'remember [key] as [value]'.")
            elif "recall" in user_input:
                key = user_input.split("recall ")[1].strip()
                print(f"{custom_name}: {self.recall(key)}")
            elif user_input == "forget":
                self.forget()
                print(f"{custom_name}: Okay, I've forgotten everything.")
                self.user_name = input("What's your name? ")
                print(f"Hello {self.user_name}! I'm {custom_name}. How can I assist you?")
            elif "time" in user_input:
                print(f"{custom_name}: The current time is {self.get_time()}.")
            elif "weather" in user_input:
                print(f"{custom_name}: I'm sorry, I cannot provide information about the weather at the moment.")
            else:
                response = self.respond(user_input, self.user_name, custom_name)
                print(f"{custom_name}:", response)

    # Method to respond to user input
    def respond(self, input, user_name, bot_name):
        doc = nlp(input)
        greetings = ["hello", "hi", "hey", "greetings"]
        farewells = ["goodbye", "bye", "see you", "take care"]
        
        if any(token.text in greetings for token in doc):
            return self.greet(user_name)
        elif any(token.text in farewells for token in doc):
            return self.farewell(user_name)
        else:
            return "I'm sorry, I didn't understand that."

# Main function to create and initiate the chatbot
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
