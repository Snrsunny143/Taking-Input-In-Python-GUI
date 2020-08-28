from tkinter import*
import sys

root = Tk()
root.title("Snr Tech And Tutorials")

input =Entry(root)
input.pack()

def printout():
    print("User Input :- "+input.get())

def quit():
    print("User Input :- Bye. ")
    print(" Meet You Later. ")
    sys.exit()

button = Button(root, text =" PrintOut ", fg = " pink " ,bg = " green ")
button.pack()

quit_button =(root, text = " Quit ", fg = "grey", bg = " pink ")
quit_button.pack()

root.mainloop()
