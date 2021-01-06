#importing libraries
#import nltk
#nltk.download()
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3 as pp
from chatterbot.trainers import ChatterBotCorpusTrainer



#for bot to speak using the pyttsx3 engine,it is an offline engine
engine = pp.init()

#for setting the speed of speech of the engine
engine.setProperty('rate', 125)

#for setting the volume of the engine
engine.setProperty('volume',1.0)

#for setting the male/female voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(word) :
    engine.say(word)
    engine.runAndWait()


#creating an instance of the chatterbot class
bot = ChatBot("My Bot")


#for clearing the previous storage of the bot everytime program is runned
#bot.storage.drop()


#for creating the listtrainer object
trainer = ListTrainer(bot)
#trainer = ChatterBotCorpusTrainer(bot)


# #training the bot
# trainer.train(
#     "chatterbot.corpus.english"
# )
trainer.train(["Hello","Hii!! How are you"])
trainer.train(["I am fine!!","Its great to hear that!!"])
trainer.train(["Who are you?","I am  bot!!"])
trainer.train(["Who created you?","I have been created by Akshat"])
trainer.train(["How are you?","I am fine,thanks for asking"])
trainer.train(["What languages you can speak?","I can talk only in english!!"])


#tkinter code

#this is the main window
main = Tk()

#for main window to open in full screen
main.attributes("-fullscreen", True)

#for closing the main window using escape key
main.bind('<Escape>',lambda e: main.destroy())

#setting the backgroundcolor of the main window
main.configure(background="#071A52")

#this specifies the title and the geometry of the main window
main.geometry("900x1300")
main.title("My chat bot")


#heading label
a = Label(main,
          text="BOT BUDDY-YOUR BUDDY FOR LIFE",
          font =("comic sans ms", 30),
          bg="#071A52").place(x=400,y=50)


#this adds the pic of a robot to the window
#ImageTk and Image packages were required because tkinter at times does not support jpg and jpeg files
img = ImageTk.PhotoImage(Image.open("bot.jpg"))
PhotoL = Label(image = img)
PhotoL.pack(pady=130)


#take query : it takes audio as input from user and converts it into string

#funtion to get the response in the reply text feild
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)


#this make the frame inside the main window
frame = Frame(main,
              bg='white')


#this is for the scrollbar
sc = Scrollbar(frame)


#this is for the message box to get the replies
msgs = Listbox(frame,
               width = 50,
               height =10,
               yscrollcommand=sc.set,
               font =("Verdana", 15),
               bg='#BDC3C7',bd=4)


#for packing the scrollbar,frame and listbox
sc.pack(side = RIGHT,
        fill = Y)
msgs.pack(side=LEFT,
          fill = BOTH ,
          pady = 0)
frame.pack( pady =0)


# creating text feild to ask questions
textF = Entry(main,
              font=("Verdana", 20),
              bg='white',bd=4)
textF.pack(pady = 10)


# creating button that evokes the function for the response
btn = Button(main,
             text="Ask the BOT",
             font=("comic sans ms", 20),
             command = ask_from_bot,
             relief = 'raised',
             bd=4,
             activebackground='cyan')
btn.pack()


#binding the enter key with the button
def enter_function(event) :
    btn.invoke()
main.bind('<Return>',enter_function)


#mainloop for the tkinter window
main.mainloop()

