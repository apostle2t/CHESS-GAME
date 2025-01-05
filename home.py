from tkinter import *
from compMain import *
from pMain import *


class windowTwo:
   def windowTwo(self):

      window1 = Tk()
      window1.geometry("420x420")
      window1.title("UE CHESS")
      window1.config(background="#3e3b34")

      label = Label(window1, text="WELCOME CHOOSE TO PLAY",
                    font=("Ariel", 25, 'bold'),
                    background="#eee9de",
                    width= 50,
                    height=10)

      label.place(x=150, y=10)

      button1 = Button(window1, text="TWO PLAYER", font=("Ariel", 18),
                      command= lambda : (window1.destroy(),playerMain()),
                      width=30,
                      height=2,
                      background="#FF6F61")
      button1.place(x=430,y=450)

      button2 = Button(window1, text="COMPUTER", font=("Ariel", 18),
                      command= lambda : (window1.destroy(),main()),
                      width=30,
                      height=2,
                      background="#FF6F61",
                       )

      button2.place(x=430,y=550)

      window1.mainloop()