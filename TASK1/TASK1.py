print("======ChatBot=====")
while True:
     user=input("you: ").lower()
     if user in ["hi", "hello", "hey", "good morning", "good evening"]:
       print("Bot: Hello! How can I help you today?")


     elif "your name" in user:
       print("Bot: My name is SmartBot.")


     elif "your age" in user or "how old are you" in user:
       print("Bot: I don't have an age because I am a chatbot.")


     elif "who created you" in user:
       print("Bot: I was created as a Python project.")


     elif "weather" in user:
       print("Bot: I cannot check live weather, but it is important to stay prepared.")

     elif "time" in user:
       print("Bot: Let me check the current time.")


     elif "date" in user:
       print("Bot: Let me check today's date.")

      
     elif "college" in user:
       print("Bot: College helps students gain knowledge and practical experience.")


     elif "education" in user:
       print("Bot: Education is the key to lifelong learning.")


     elif "python" in user:
       print("Bot: Python is one of the most popular programming languages.")


     elif "java" in user:
       print("Bot: Java is an object-oriented programming language.")


     elif "c language" in user or "c programming" in user:
       print("Bot: C is a powerful procedural programming language.")


     elif "ai" in user or "artificial intelligence" in user:
       print("Bot: AI enables machines to perform tasks that normally require human intelligence.")


     elif "machine learning" in user:
       print("Bot: Machine Learning is a subset of Artificial Intelligence.")


     elif "data science" in user:
       print("Bot: Data Science involves extracting insights from data.")


     elif "sql" in user:
       print("Bot: SQL is used to manage and query databases.")


     elif "motivate me" in user:
       print("Bot: Every expert was once a beginner. Keep learning!")


     elif "success" in user:
       print("Bot: Success comes from consistency and hard work.")


     elif "joke" in user:
       print("Bot: Why do programmers hate nature? Too many bugs!")


     elif "study tips" in user:
       print("Bot: Study regularly, revise often, and practice problems.")


     elif "gate" in user:
       print("Bot: GATE is a national-level engineering entrance examination.")


     elif "favorite color" in user:
       print("Bot: I like all colors because I am a virtual assistant.")


     elif "favorite food" in user:
       print("Bot: I don't eat food, but pizza sounds popular!")


     elif "sports" in user:
       print("Bot: Sports improve fitness and teamwork skills.")


     elif "cricket" in user:
       print("Bot: Cricket is one of the most popular sports in India.")
    

     elif "music" in user:
       print("Bot: Music can improve mood and concentration.")


     elif "friend" in user:
       print("Bot: Good friends support and encourage each other.")


     elif "happy" in user:
       print("Bot: Happiness grows when shared with others.")


     elif "sad" in user:
       print("Bot: Difficult times pass. Keep moving forward.")


     elif "thank" in user:
       print("Bot: You're welcome!")


     elif "help" in user:
       print("Bot: Ask me about programming, studies, AI, sports, jokes, motivation, and more.")


     elif user in ["bye", "goodbye", "exit", "quit"]:
       print("Bot: Goodbye! Have a great day!")
       break