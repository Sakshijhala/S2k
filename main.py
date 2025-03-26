import sys
import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import pyjokes
import subprocess
import pyautogui
import psutil
import winshell
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
from index import*
import socket
import imdb
from GoogleNews import GoogleNews
import pandas as pd
import string
from cal import*

def password():
    char = string.ascii_letters + string.digits
    ret = ''.join(random.choice(char) for x in range(0,15))
    print(ret)

def news():
    news = GoogleNews(period='1d')
    news.search("India")
    result = news.result()
    #print(result)
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=("img"))
    data.head()
    for i in result:
        speak(i.get("title", "No title available"))
    

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=10)
        try:
            print("Recognizing.....")
            query=r.recognize_google(audio)
            print(f"User said:{query}\n")
        except Exception as e:
            speak("Unable to recognize your Voice.....")
            return"None"
        return query
def username():
    speak("what should I call you mam?")
    Uname=takeCommand()
    speak(f"Welcome Miss {Uname}")
    speak("how can I help you, mam?")
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Morning !")
    else:
        speak("Good Evening !")
    speak("I am your Virtual assitant alpha")
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=str(psutil.sensors_battery())
    speak("cpu is at"+battery)
    
def movie():
    moviesdb = imdb.IMDb()

    speak("Please tell me the movie name, mam.")
    text = takeCommand()
    
    movies = moviesdb.search_movie(text)
    speak(f"Searching for {text}...")
    
    if not movies:
        speak("No result found.")
    else:
        speak("I found these:")
        
        for m in movies:  # Changed variable name to avoid conflict
            title = m.get("title", "Unknown Title")  # Correct way to get attributes
            year = m.get("year", "Unknown Year")
            
            speak(f"{title} - {year}")
            
            movie_id = m.getID()  # Get movie ID
            movie_info = moviesdb.get_movie(movie_id)  # Fetch movie details
            
            rating = movie_info.get("rating", "No Rating Available")
            plot = movie_info.get('plot outline', "Plot not available")
            
            current_year = int(datetime.datetime.now().strftime("%Y"))
            
            if isinstance(year, int) and year < current_year:
                speak(f"{title} was released in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}")
            else:
                speak(f"{title} will be released in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}")
            
            break  
def rock():
    you= int(input("please enter your choice!- \n 1-Rock \n2-Paper \n3-Scissor"))
    shapes = {1:'rock', 2:'paper', 3:'scissor'}
    if you not in shapes:
        print("Please enter valid number")
        exit()
    comp=random.randint(1,3)
    print("you choose", you)
    print("computer choose", comp)
    if(you==1) and (comp==3) or (you == 2) and (comp==1) or (you==3) and (comp==2):
        speak("congratulations you won!")
    elif(you==comp):
        speak("match tied")
    else:
        speak("you loose")

def count():
    t = int(input("Enter time in seconds! "))
    while t:
        min,secs = divmod(t,60)
        timer = '(:02d):(:02d)'.format(min, secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
        print("\n")
        
def guess():
    start=1
    end=1000
    value= random.randint(start,end)
    print("The computer choose a number between", start, "and", end)
    guess= None
    while guess != value:
        text =input("Guess the number: ")
        guess = int(text)
        if guess< value:
            speak("The number is higher")
            
        elif guess> value:
            speak("The number is lower")   
    speak("Congratulations! you won")             
        
    
    
    
if __name__ == '__main__':
    wishme()
    username()
    while True:
        order = takeCommand().lower()
        
        if 'how are you' in order:
            speak("I am fine, Thankyou")
            speak("how are you")
        elif 'fine' in order or 'good' in order:
            speak("it's good to know you are fine")
        elif 'who i am' in order:
            speak("if you can talk then surely you are as human")
        elif 'love' in order:
            speak("it is the 7th sense that destroy all other senses")
        elif 'who are you' in order:
            speak("i am your virtual assistant")
        elif 'i love you' in order:
            speak("oh my god! thankyou, i love you too")
        elif 'what is your name' in order:
            speak("my friends call me Alpha")
        elif 'open notepad' in order:
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            
        elif 'play music' in order or 'play songs' in order:
            music_dir="C:\\Users\\Meena Jhala\\Music\\music"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
            
        elif 'wikipedia' in order:
            speak('searching.....')
            query = "order"
            search_results = wikipedia.search(query)
            order=order.replace("wikipedia","")
            results=wikipedia.summary(order,sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open google' in order:
            speak("here you go to google mam\n")
            webbrowser.open("google.com")
            
        elif 'open myntra' in order:
            speak("here you go to myntra mam. Happy shopping\n")
            webbrowser.open("myntra.com")
            
        elif 'open youtube' in order:
            speak("here you go to youtube mam")
            webbrowser.open("youtube.com")
            
        elif 'open amazon' in order:
            speak("here you go to amazon mam. Happy shopping")
            webbrowser.open("amazon.in")
            
        elif 'open stackoverflow' in order:
            speak("here you go to stack overflow. blow your coding skill")
            webbrowser.open("stackoverflow.com")
            
        elif "where is" in order:
            order=order.replace("where is", "")
            location=order
            speak("locating...") 
            speak("location....")
            webbrowser.open(f"https://www.google.co.in/maps/place/{location}")
            
        elif "write a note" in order:
            speak("what should i write mam")
            note=takeCommand()
            file=open("jarvis.txt",'w')
            speak("mam, Should i include date and time as well")
            sn=takeCommand()
            if 'yes'in sn or 'sure' in 'yeah' in sn:
                strTime=datetime.datetime.now().strftime("%H:%M:S")
                file.write(strTime)
                file.write(note)
                speak("Done mam")
            else:
                file.write(note)
                speak("Done mam")
            
        elif 'show note' in order:
            speak("showing notes")
            file=open("jarvis.txt",'r')
            print(file.read())
            speak(file.read(6))
            
        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en", category="neutral"))
            
        elif 'the time' in order:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"well, the time is {strTime}")
                    
        elif 'shutdown' in order or 'turn off' in order:
            speak("Hold on a second mam! your system is on its way to shutdown")
            speak("make sure all of your application are closed")
            time.sleep(5)
            subprocess.call(['shutdown', '/s'])
            
        elif 'restart' in order:
            subprocess.call(['shutdown','/r'])
            
        elif 'hibernate' in order:
            speak("hibernating....")
            subprocess.call(['shutdown','/h'])
            
        elif 'log off' in order or 'sign out' in order:
            speak("make sure all of your application are closed before sign out")
            time.sleep(5)
            subprocess.call(['shutdown', '/l'])
            
        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('txt')
            time.sleep(1)
            pyautogui.keyUp('alt')
            
        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak('mam, please tell me the name for this file')
            name=takeCommand().lower()
            speak('please hold the screen')
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured mam")
            
        elif 'cpu status' in order:
            cpu()
            
        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
            speak("recycle bin recycled")
            
            
        elif 'camera' in order:
             cam()
             
            
        elif 'exit'in order or 'quit' in order:
            speak("Thankyou! for using me mam. Have a good day!!")
            sys.exit()
            
        elif 'ip' in order:
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            speak("your IP address is" +ip)
            
        elif 'bmi' in order:
            speak("Please tell your height in centimeter")
            height=takeCommand()
            speak("Please tell your weight in kilogram")
            weight=takeCommand()
            height=float(height)/100
            weight = float(weight)
            BMI=float(weight)/(height*height)
            speak("Your Body Mass index is " +str(BMI))
            if (BMI>0):
                if (BMI<=16):
                    speak("You are severly underweight")
                elif(BMI<=18.5):
                    speak("you are underweight")
                elif(BMI<=25):
                    speak("you are Healthy")
                elif(BMI<=30):
                    speak("you are overweight")
                else:
                    speak("you are severly overweight")
                    
            else:
                speak("Enter valid details")        
                
        elif 'movie' in order:
            movie() 
            
        elif 'news' in order:
            news()
            
        elif 'password' in order:
            password()
            
        elif 'rock' in order:
            rock()
            
        elif 'guess' in order:
            guess()
            
        elif 'countdown' in order:
            count()
        elif 'calendar' in order:
            show_calendar()
            
            
                
                   
                
            