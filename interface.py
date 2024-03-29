
# import tkinter

# window = tkinter.Tk()
# window.title("GUI")

# # creating 2 frames TOP and BOTTOM
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# # now, create some widgets in the top_frame and bottom_frame
# btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack(side = "left")# 'fg - foreground' is used to color the contents
# btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack(side = "right")# 'text' is used to write the text on the Button
# btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
# btn4 = tkinter.Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

# window.mainloop()
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()