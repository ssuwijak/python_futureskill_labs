import tabnanny # unknown lib (auto import by vscode extesion)
import speech_recognition as sr # voice to text lib .. pip install SpeechRecognition 
import pyttsx3 # off-line text to voice lib .. pip install pyttsx3
import webbrowser  # built-in lib
import datetime  # built-in lib
import time  # built-in lib
# to use microphone requires .. pip install PyAudio  

def greeting():
    msg = ""
    hr = datetime.datetime.now().hour
    if hr >= 0 and hr < 12:
        msg = "good morning"
    elif hr >=12 and hr < 15:
        msg = "good afternoon"
    else:
        msg = "good evening"

    msg = "hello, " + msg
    speak(msg)
   

def speak(msg):
    print(msg)
    tts.say(msg)
    tts.runAndWait()

def takeCmd():
    cmd = ""
   
    with sr.Microphone() as mic:
        recog.adjust_for_ambient_noise(mic) # auto reduce ambient noise
        print("i'm listening ... within 5 sec.")
        voice = recog.listen(mic, timeout = 5) # waiting for listening within 5 sec.
        
        try:
            cmd = recog.recognize_google(voice) # use google voice2text lib
            speak("ok, you said '" + cmd + "'.")
        except Exception as ex:
            speak("sorry, please say again.")
            cmd = "None"
        
    return cmd


recog = sr.Recognizer()

tts = pyttsx3.init()
tts.setProperty("rate", 170) # set speak slowly
tts.setProperty("volume", 1.0) # set loudness
voices = tts.getProperty("voices") # check voice types, male/female
tts.setProperty("voice", voices[1].id) # select voice type


speak("loading your AI personal assistant ...")
greeting()
speak("i'm ready. may i help you ?")

while True:
    cmd = takeCmd().lower()
    
    if "goodbye" in cmd or "stop" in cmd or "bye" in cmd:
        speak("i'm closing myself, see you later ... bye")
        break
    elif "youtube" in cmd:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("YouTube has been opened")
    elif "google" in cmd:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google has just been opened")
    elif "time" in cmd:
        t = datetime.datetime.now().strftime("%H:%M:%S")
        speak("now is " + t)
    elif "how are you" in cmd:
        speak("not bad.")
    elif "hello" in cmd:
        speak("henlo, what's up man ?")
    elif "none" in cmd:
        continue
    else:
        speak("i don't understand your command.")
    
    # print("wait for the new command within 3 seconds")
    t = 3
    print("wait for 3 sec.")
    time.sleep(t)

