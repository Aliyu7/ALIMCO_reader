from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter import PhotoImage
import pyttsx3
import os
import PyPDF2

import multiprocessing


#---------------------------------------------------------------------
# Main Window
#---------------------------------------------------------------------
root = Tk()

root.title("ALIMCO MP3 Player")

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------
my_book = []
def openBook():
    global book
    global pages
    global myReader
    file = filedialog.askopenfilename()
    if file.endswith(".pdf"):
        book = open(file, 'rb')
        myReader = PyPDF2.PdfFileReader(book)
        pages = myReader.numPages
        print(pages)

        my_book.insert
def playBook():
    for num in range(0, pages):
        page = myReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


def stopBook():
    speaker.stop
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------

label = Label(root, text="               This is ALIMCO Reader              ")
add_book_button = Button(root, text="select book", command = openBook)
red_book_button = Button(root, text="Read", command = playBook)

label.pack()
add_book_button.pack()
red_book_button.pack()




mainloop()
