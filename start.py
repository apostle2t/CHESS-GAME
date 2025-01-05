from tkinter import *
from home import windowTwo
class windowOne:
    def __init__(self):
        self.window = Tk()

    def manclose(self):
        self.window.destroy()
    def windowOne(self):
        self.window.geometry("420x420")
        self.window.title("UE CHESS")
        self.window.config(background="#3e3b34")
        #self.window.iconphoto()

        canvas = Canvas(self.window, height=300, width=1000,background="#eee9de")
        center_x, center_y = 500,250
        text_x, text_y = 500,250
        radius = 200


        canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline="black", fill="#736ec4"
        )

        canvas.create_text(
            text_x, text_y,  # Position of the text
            text="UE CHESS",  # Text to display
            font=("Arial", 50, "bold"),  # Font (optional)
            fill="black"  # Text color (optional)
        )

        canvas.pack()

        button = Button(self.window, text="Click to get started",font=("Ariel",18),
                        command= lambda: (self.manclose(),new2.windowTwo()),
                        width=30,
                        height=60,
                        background="#FF6F61")
        button.pack(pady=140)
        self.window.mainloop()


new2 = windowTwo()
