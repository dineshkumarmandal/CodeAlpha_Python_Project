#Type of chatbots
#1. Rule-Based Chatbots ..... Rules .... Patterns and Response (Input and Output).
#2. Self-Learning Chatbots ...... ML - Deep Learning - NLP
#---------------------------------------------
#installing nltk library
#pip install nltk 
#importing Required Libraries
import nltk
from nltk.chat.util import Chat, reflections
#Creating questions and answers (input and output) ...... (Logic for the NLTK chatbot)
pairs = [
    [
        r"Hello|Hi|Hey",
        ["Hello, How are you today ? "]
    ],
    [
        r"I'm fine",
        ["Glad to hear that, how can I help you ? "]
    ],
    [
        r"How are you ? ",
        ["I'm good. "]
    ],
    [
        r"Who are you ? ",
        ["I'm a NLTK chatbot"]
    ],
    [
        r"What is your name ? ",
        ["My name is AI Mandal"]
    ],
    [
        r"I want to know about Machine Learning.",
        ["Sure, You can checkout link https://en.wikipedia.org/wiki/Machine_learning"]
    ],
    [
        r"I want to know about ML.",
        ["Sure, You can checkout link https://en.wikipedia.org/wiki/Machine_learning"]
    ],
    [
        r"Thanks",
        ["You are welcome"]
    ],
    [
        r"Exit",
        ["It was my pleasure to help you, Please come again!"]
    ]
]
# a dictionary containing basic input and corresponding outputs
reflections
#default message for starting chat
print("Please, Write anything to start chat")
#Creating chat bot
chat = Chat(pairs)
#Start Conversation
chat.converse()