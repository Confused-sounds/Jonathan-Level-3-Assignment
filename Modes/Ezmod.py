import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog

windr = tk.Tk()
windr.title("Easy")
windr.geometry("300x300")
messagebox.showinfo(
    "EZ",
    "Easy Mode Selected",
)


def go_home():
    windr.destroy()
    import main
    main


complete = False
Score = 0
Question = 0
List = []
while complete == False:
    Add1 = random.randint(1, 10)
    Add2 = random.randint(1, 10)
    Ans1 = Add1 + Add2
    List.append(Ans1)
    Question += 1
    Ques1 = simpledialog.askinteger(
        "Question {}, Score {}/10".format(Question, Score),
        "What is {} + {} ".format(Add1, Add2))

    if Question == 10:
        messagebox.showinfo("Game Over",
                            "Game Over, Your Score Was {}/10".format(Score))
        List = []
        complete = True
    elif Ques1 in List:
        Score += 1
        messagebox.showinfo("Correct", "Correct, +1 Score!")
        List = []

    else:
        messagebox.showerror("WRONG", "Incorrect")
        List = []

nutt = tk.Button(text="Home", command=go_home)
nutt.pack()


def go_home():
    windr.destroy()
    import main
    main


nutt = tk.Button(text="Home", command=go_home)
nutt.pack()
