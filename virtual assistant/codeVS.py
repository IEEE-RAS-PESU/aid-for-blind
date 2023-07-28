
from tkinter import *
import webbrowser as wb
import speech_recognition as sr
import pyttsx3 as pt
import pyjokes
import time
import googletrans
from translate import Translator
import pywhatkit

root=Tk()
root.title("PYTHON ASSISTANT")



def assist():
    text=pt.init()
    r=sr.Recognizer()
    text.say("hello. i am your virtual assistant ")
    text.say("what can i do for you")
    text.runAndWait()
    
    
    with sr.Microphone() as source:
        audio=r.listen(source)
        
        try:
            ans=r.recognize_google(audio)
            if "name" in ans.lower():
                text.say("your name is sharan")
                text.runAndWait()
            elif "search" in ans.lower():
                a=ans.split()
                n=a[len(a)-1]
                wb.open_new('https://www.google.com/search?q='+n+
                            '&ei=dozzYb2sGJ7H4-EP0uWeoA8&ved='+
                            '0ahUKEwi9v6aQ6NP1AhWe4zgGHdKyB_'+
                            'QQ4dUDCA4&uact=5&oq=flowers&gs_lcp='+
                            'Cgdnd3Mtd2l6EAMyCAgAELEDEJECMggIABCxAx'+
                            'CRAjIICAAQgAQQsQMyCAguELEDEJECMgUIABCABDIF'+
                            'CAAQgAQyBQgAEIAEMgUIABCABDIKCAAQgAQQsQMQCjI'+
                            'ICAAQgAQQsQM6BwgAELADEAo6CwgAELADEAcQChAeSg'+
                            'QIQRgBSgQIRhgAUNkDWNkDYL8JaAFwAHgAgAFqiAFq'+
                            'kgEDMC4xmAEAoAEByAEGwAEB&sclient=gws-wiz')
                text.say("searching"+n)
                text.runAndWait()
            elif "joke" in ans.lower():
                My_joke = pyjokes.get_joke(language="en", category="neutral")
                time.sleep(1)
                print("The joke is:")
                text.say(My_joke)
                text.runAndWait( )
                print(My_joke)
            elif "song" in ans.lower():
                text.say("which song do ypu want to play")
                text.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    try:
                        song=r.recognize_google(audio)
                        pywhatkit.playonyt(song)
                        text.say("paying"+song+"on youtube")
                        text.runAndWait()
                    except():
                        text.say("could not recognise the song name")
                        text.runAndWait()
            elif "video" in ans.lower():
                text.say("which video do ypu want to play")
                text.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    try:
                        video=r.recognize_google(audio)
                        pywhatkit.playonyt(video)
                        text.say("paying"+video+"on youtube")
                        text.runAndWait()
                    except():
                        text.say("could not recognise the song name")
                        text.runAndWait()
            elif "bye" in ans.lower():
                text.say("bye.have a nice day")
                text.runAndWait()
                
            else:
                text.say("this is out of my reach. sorry")
                text.runAndWait()
            
        except:
            text.say("sorry could not recognize your voice") 
            text.runAndWait()
    

b1=Button(root,text="speak ",command=assist,fg="blue",bg="yellow")
b1.pack()

b2=Button(root,text="close",command=root.destroy,bg="red")
b2.pack()

root.mainloop()