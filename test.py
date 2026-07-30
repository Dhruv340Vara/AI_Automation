from modules.ai_engine import AIEngine

ai=AIEngine()

while True:
    command=input("You : ")

    if command=="exit":
        break

    print(ai.process(command))
