from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open('R:\Projects_Python\Golems_Rush\Bg.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


main_form = Tk()
app = Window(main_form)
main_form.title("Golems_Rush")
main_form.geometry('626x469')
main_form.resizable(False, False)
#Button(text="Button", width=20).pack()
main_form.mainloop()

