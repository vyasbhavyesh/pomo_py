# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:46:18 2018

@author: bhavyas
"""
import tkinter as tk
from tkinter import font  as tkfont
import speech_recognition as sr
from pygame import mixer
import pyperclip
import threading
import pyttsx3
import time

cmd = ''
def thr():
    t1 = threading.Thread(target=buttonClick, daemon=True)
    t1.start()

def buttonClick():

    # using the pygame mixer to play sound effects, 'prompting' the user to speak
    engine = pyttsx3.init()
    engine.say('Press Voice input and tell Where to navigate after the beep')
    engine.runAndWait()
    time.sleep(1)
    
    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    # starting the recognizer, with some optional parameters that I found work well

    r = sr.Recognizer()                                         
    r.pause_threshold = 0.7                                     
    r.energy_threshold = 400
    
    with sr.Microphone() as source:
        
        try:
            
            audio = r.listen(source, timeout=5)

            # use your own API key. get it here https://cloud.google.com/speech/

            message = str(r.recognize_bing(audio, key='4ee80d226a9e4b64ae765a4d2473a991')) 

            # playing the sound effect after recognition completed 

            mixer.music.load('chime2.mp3')
            mixer.music.play()

            # placing the recognized 'message' on the clipboard

            pyperclip.copy(message)
            global cmd 
            print(message)
            cmd = message
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        else:
            pass
        
        

class pomo_py(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('1080x720')
        self.title("Welcome to PomoPy")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
    def voice_navigate(self):
       
        if 'go to' in cmd.lower() or 'page one' in cmd.lower():
            frame = self.frames["PageOne"]
            frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        record_button = tk.Button(self, text = 'Voice input', width=50, command=thr)
        print (cmd)
        if 'go to' in cmd.lower() or 'page one' in cmd.lower():
             controller.show_frame("PageOne")
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        record_button.pack()
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




if __name__ == "__main__":
    app = pomo_py()
    
    app.mainloop()




