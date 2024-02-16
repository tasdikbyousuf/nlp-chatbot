import random
import spacy

nlp = spacy.load("en_core_web_sm")

class Chatbot:
    def __init__(self):
        self.memory = {}
        self.user_name = ""

    def greet(self, name):
        responses = [f"Hello {name}!", f"Hi {name}!", f"Hey {name}!", f"Greetings {name}!"]
        return random.choice(responses)

    def farewell(self, name):
        responses = [f"Goodbye {name}!", f"See you later {name}!", f"Bye {name}!", f"Take care {name}!"]
        return random.choice(responses)

    def sentiment_analysis(self, text):
        doc = nlp(text)
        sentiment_score = doc.sentiment
        if sentiment_score >= 0.5:
            return "That sounds positive!"
        elif sentiment_score <= -0.5:
            return "That sounds negative."
        else:
            return "I'm not sure about the sentiment."

    def named_entity_recognition(self, text):
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "I don't remember anything about that.")

    def forget(self):
        self.memory = {}
        self.user_name = ""

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
            if user_input == "exit":
                print(self.farewell(self.user_name))
                break
            elif user_input == "what can you do":
                print(f"{custom_name}: I can respond to greetings, farewells, perform sentiment analysis, and named entity recognition. I can also remember things. Feel free to ask me anything!")
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
            else:
                response = self.respond(user_input, self.user_name, custom_name)
                print(f"{custom_name}:", response)

    def respond(self, input, user_name, bot_name):
        doc = nlp(input)
        greetings = ["hello", "hi", "hey", "greetings"]
        farewells = ["goodbye", "bye", "see you", "take care"]
        
        if any(token.text in greetings for token in doc):
            return self.greet(user_name)
        elif any(token.text in farewells for token in doc):
            return self.farewell(user_name)w
        else:
            return "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
