# chatbot_pairs.py
introduction_convo = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello|hola",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How can I assist you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to hear that!", "Alright, great!",]
    ],
    [
        r"quit",
        ["It was nice talking to you. Goodbye "]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ],
]
