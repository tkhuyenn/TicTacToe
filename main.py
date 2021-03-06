import tkinter.messagebox
from tkinter import *

#Tạo cửa sổ
root = Tk()
root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth(), root.winfo_screenheight()))


root.title("Tic Tac Toe")
root.configure(background='lightcyan')

Tops = Frame(root, bg='lightcyan', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)


#Tạo label tên game
lblTitle = Label(Tops, font=('Lucida Handwriting', 50, 'bold'), text="Tic Tac Toe Game", bd=21, bg='lightcyan', fg='black',
                 justify=CENTER)
lblTitle.grid(row=0, column=0)

# Tạo MainFrame
MainFrame = Frame(root, bg='lightcyan', bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

#Tạo LeftFrame trong MainFrame
LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg='lightcyan', relief=RIDGE)
LeftFrame.pack(side=LEFT)

#Tạo RightFrame trong MainFrame
RightFrame = Frame(MainFrame, bd=10, width=560, height=600, pady=10, padx=2, bg='lightcyan', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=10, padx=2, bg='lightcyan', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=10, padx=2, bg='lightcyan', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

# Khai báo PlayerX, PlayerO là 1 số nguyên, gán giá trị mặc định bằng 0
PlayerX = IntVar()
PlayerO = IntVar()

# Khai báo button dưới dạng chuỗi
buttons = StringVar()

# Khai báo biến click, giá trị mặc định là True
# click = True ==> Lượt X
# click = False ==> Lượt O
click = True


# Hàm kiểm tra lượt đi là của X hay O và hiển thị
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()


# Hàm kiểm tra và thêm điểm cho người thắng, nếu hòa thì chơi lại
def scorekeeper():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        reset()
        return

    if (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return

    if (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        reset()
        return


    if (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and button4["text"] != " " and
            button5["text"] != " " and button6["text"] != " " and button7["text"] != " " and button8["text"] != " " and
            button9["text"] != " "):
        tkinter.messagebox.showinfo("Tie game", "The game is over")
        reset()
        return

# Hàm bắt đầu lại lượt chơi
def reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "

    button1.configure(background='#5F9EA0')
    button2.configure(background='#5F9EA0')
    button3.configure(background='#5F9EA0')
    button4.configure(background='#5F9EA0')
    button5.configure(background='#5F9EA0')
    button6.configure(background='#5F9EA0')
    button7.configure(background='#5F9EA0')
    button8.configure(background='#5F9EA0')
    button9.configure(background='#5F9EA0')

# Hàm bắt đầu lại trò chơi
def NewGame():
    reset()

    PlayerX.set(0)
    PlayerO.set(0)


# Tạo label PlayerX
lblPlayerX = Label(RightFrame1, font=('Lucida Handwriting', 40), text="Player X:", padx=2, pady=2, bg='lightcyan')
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('Lucida Handwriting', 40), bd=2, fg='black', textvariable=PlayerX, width=14,
                   justify=LEFT).grid(row=0, column=1)

# Tạo label PlayerO
lblPlayerO = Label(RightFrame1, font=('Lucida Handwriting', 40), text="Player O:", padx=2, pady=2, bg='lightcyan')
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font=('Lucida Handwriting', 40), bd=2, fg='black', textvariable=PlayerO, width=14,
                   justify=LEFT).grid(row=1, column=1)

# Tạo nút Newgame
btnNewgame = Button(RightFrame2, text="New Game", font=('Lucida Handwriting', 26), height=3, width=32, bg='#5F9EA0',
                    command=NewGame)
btnNewgame.grid(row=0, column=0, padx=6, pady=10)


# Tạo nút Reset
btnReset = Button(RightFrame2, text="Reset", font=('Lucida Handwriting', 26), height=3, width=32, bg='#5F9EA0', command=reset)
btnReset.grid(row=1, column=0, padx=6, pady=10)

# Tạo các buttons để hiển thị lượt đi
button1 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(LeftFrame, text=" ", font=('Lucida Handwriting', 26), height=4, width=8, bg='#5F9EA0',
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)


root.mainloop()
