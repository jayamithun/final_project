import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def two():
    call(["python", "2048.py"])
def hangman():
    call(["python", "hangman.py"])
def mem_game():
    call(["python", "memory game.py"])
def pacman():
    call(["python","pacman.py"])
def Flappy():
    call(["python","Flappy.py"])
def xo():
    call(["python","Tic-Tac-Toe.py"])
def tile():
    call(["python","Tile15.py"])
def catch():
    call(["python","Catch-The-Ball.py"])

class game_box:
    def __init__(self):
        root = Tk()
        _bgcolor = '#ffffff'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("GAME BOX")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''GAME BOX''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.17, height=93, width=230)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''play 2048''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=two)

        self.Button9 = Button(self.Frame1)
        self.Button9.place(relx=0.53, rely=0.17, height=93, width=230)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(disabledforeground="#bfbfbf")
        self.Button9.configure(font=font14)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''play 15 Tile''')
        self.Button9.configure(width=566)
        self.Button9.configure(command=tile)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.33, height=93, width=230)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''play hangman''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=hangman)

        self.Button10 = Button(self.Frame1)
        self.Button10.place(relx=0.53, rely=0.33, height=93, width=230)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(disabledforeground="#bfbfbf")
        self.Button10.configure(font=font14)
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''play Tic Tac Toe''')
        self.Button10.configure(width=566)
        self.Button10.configure(command=xo)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.47, height=93, width=230)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''play memory game''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=mem_game)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.61, height=93, width=230)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''play pacman''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=pacman)


        self.Button7 = Button(self.Frame1)
        self.Button7.place(relx=0.53, rely=0.61, height=93, width=230)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(disabledforeground="#bfbfbf")
        self.Button7.configure(font=font14)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''play flappy''')
        self.Button7.configure(width=566)
        self.Button7.configure(command=Flappy)

        self.Button8 = Button(self.Frame1)
        self.Button8.place(relx=0.53, rely=0.47, height=93, width=230)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(disabledforeground="#bfbfbf")
        self.Button8.configure(font=font14)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''play catch the ball''')
        self.Button8.configure(width=566)
        self.Button8.configure(command=catch)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.35, rely=0.77, height=103, width=230)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''EXIT''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=game_box()


