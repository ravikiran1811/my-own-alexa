import speech_recognition as sr
import pyttsx3
import pywhatkit
import  datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

engine.say("i'm your dev")
engine.say("How can i help you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def talk_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dev' in command:
                command = command.replace('dev','')
                print(command)

    except:
        pass
    return  command
def run_dev():
    command = talk_command()
    if 'play' in command:
        song = command.replace('play','')
        print('Playing...')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+ time)
    elif 'few lines about' in command:
        person = command.replace('say few lines about','')
        info = wikipedia.summary(person,10)
        print(info)
        talk(info)
    elif 'date with me' in command:
        talk('sorry,I am in work now can we plan next time')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('say it again')
while True:
    run_dev()
