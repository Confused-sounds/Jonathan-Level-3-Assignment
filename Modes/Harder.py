import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog

windr = tk.Tk()
windr.title("Hard")
windr.geometry("300x300")
messagebox.showinfo(
    "Herd",
    "Hard Mode Selected",
)

swap = False


def go_home():
    windr.destroy()
    import main
    main


complete = False
Score = 0
Question = 0
List = []
while complete == False:
    Add1 = random.randint(20, 50)
    Add2 = random.randint(20, 50)
    Thingy = random.randint(1, 3)
    if Thingy == 1:
        Ans1 = Add1 + Add2
        List.append(Ans1)
        Question += 1
        Ques1 = simpledialog.askinteger(
            "Question {}, Score {}/15".format(Question, Score),
            "What is {} + {} ".format(Add1, Add2))
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            List = []

        else:
            messagebox.showerror("WRONG", "Incorrect")
            List = []

    elif Thingy == 2:
        if Add2 > Add1:
            Ans2 = Add2 - Add1
            swap = True
        elif Add1 > Add2:
            Ans2 = Add1 - Add2
        else:
            simpledialog.showerror("Err", "Error")
            break
        List.append(Ans2)
        if swap == False:
            Question += 1
            Ques1 = simpledialog.askinteger(
                "Question {}, Score {}/15".format(Question, Score),
                "What is {} - {} ".format(Add1, Add2))
        else:
            Question += 1
            Ques1 = simpledialog.askinteger(
                "Question {}, Score {}/15".format(Question, Score),
                "What is {} - {} ".format(Add2, Add1))
            swap = False
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
            List = []
            complete = True
        elif Ques1 in List:
            Score += 1
            messagebox.showinfo("Correct", "Correct, +1 Score!")
            List = []

        else:
            messagebox.showerror("WRONG", "Incorrect")
            List = []
    else:
        Add3 = random.randint(10, 20)
        Add4 = random.randint(5, 10)
        Ans1 = Add3 * Add4
        List.append(Ans1)
        Question += 1
        Ques1 = simpledialog.askinteger(
            "Question {}, Score {}/10".format(Question, Score),
            "What is {} x {} ".format(Add3, Add4))
        if Question == 15:
            messagebox.showinfo(
                "Game Over", "Game Over, Your Score Was {}/15".format(Score))
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
