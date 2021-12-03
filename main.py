import pyttsx3 as py
import datetime
import os
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser

engine = py.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
# male voice 0
# female voice 1

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Radhe Radhe!")
    elif hour >= 12 and hour < 12:
        speak("Good Afternoon Radhe Radhe!")
    else:
        speak("Good Evening Radhe Radhe!")

    speak("I am your assistent Sir, Please tell me how may I help you")


def takeCommand():
    # it take the command from the microphone by user voice and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on the query
        # if wikipedia found in the query then this block will be executed
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open Instagram' in query:
            webbrowser.open("Instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Thakur\\Music\\music\\SONG 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play video songs' in query:
            video_dir = "D:\\SONG\\a"
            songs = os.listdir(video_dir)
            print(songs)
            os.startfile(os.path.join(video_dir, songs[1]))
        elif 'play video lecture' in query:
            video_Lecture_dir = "D:\\Python whole tutorial\\Chapter_0_introduction_to_python"
            songs = os.listdir(video_Lecture_dir)
            print(songs)
            os.startfile(os.path.join(video_Lecture_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\Thakur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)