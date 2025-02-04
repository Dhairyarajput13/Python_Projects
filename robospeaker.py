import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    print("Welcome to the Robo Speaker 1.1 Created by Dhairya Rajput")

    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            engine.say("Bye bye friend")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()
