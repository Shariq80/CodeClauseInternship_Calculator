import tkinter
from tkinter import *
from tkinter import messagebox

var = ""
A = 0
operator = ""

def button1isClicked():
    global var
    var = var + "1"
    theData.set(var)
def button2isClicked():
    global var
    var = var + "2"
    theData.set(var)
def button3isClicked():
    global var
    var = var + "3"
    theData.set(var)
def button4isClicked():
    global var
    var = var + "4"
    theData.set(var)
def button5isClicked():
    global var
    var = var + "5"
    theData.set(var)
def button6isClicked():
    global var
    var = var + "6"
    theData.set(var)
def button7isClicked():
    global var
    var = var + "7"
    theData.set(var)
def button8isClicked():
    global var
    var = var + "8"
    theData.set(var)
def button9isClicked():
    global var
    var = var + "9"
    theData.set(var)
def button0isClicked():
    global var
    var = var + "0"
    theData.set(var)

def buttonAddisClicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    theData.set(var)

def buttonSubisClicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    theData.set(var)

def buttonMulisClicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    theData.set(var)

def buttonDivisClicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    theData.set(var)

def buttonEqualisClicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "="
    var = var + "="
    theData.set(var)

def buttonCisClicked():
    global A
    global var
    global operator
    var = ""
    A = 0
    operator = ""
    theData.set(var)

def res():
    global A
    global operator
    global var
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        theData.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        theData.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        theData.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("ERROR", "Division by 0 invalid")
            A = ""
            var = ""
            theData.set(var)
        else:
            x = A / a
            theData.set(x)
            var = str(x)
    
guiWindow = tkinter.Tk()
guiWindow.geometry("320x600+400+400")
guiWindow.resizable(0,0)
guiWindow.title("Calculator")

theData = StringVar()
guiLabel = Label(
    guiWindow,
    text = "Label",
    anchor=SE,
    font= ("Cambria Math", 24),
    textvariable=theData,
    background="#565254",
    fg="#FFFBFE"
)
guiLabel.pack(expand=True, fill="both")

frameOne = Frame(guiWindow)
frameOne.pack(expand=True, fill="both")
frameTwo = Frame(guiWindow)
frameTwo.pack(expand=True, fill="both")
frameThree = Frame(guiWindow)
frameThree.pack(expand=True, fill="both")
frameFour = Frame(guiWindow)
frameFour.pack(expand=True, fill="both")

buttonOne = Button(
    frameOne,
    text="1",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button1isClicked
)
buttonOne.pack(side=LEFT, expand=True, fill="both")

buttonTwo = Button(
    frameOne,
    text="2",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button2isClicked
)
buttonTwo.pack(side=LEFT, expand=True, fill="both")

buttonThree = Button(
    frameOne,
    text="3",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button3isClicked
)
buttonThree.pack(side=LEFT, expand=True, fill="both")

buttonC = Button(
    frameOne,
    text="C",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=buttonCisClicked
)
buttonC.pack(side=LEFT, expand=True, fill="both")

buttonFour = Button(
    frameTwo,
    text="4",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button4isClicked
)
buttonFour.pack(side=LEFT, expand=True, fill="both")

buttonFive = Button(
    frameTwo,
    text="5",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button5isClicked
)
buttonFive.pack(side=LEFT, expand=True, fill="both")

buttonSix = Button(
    frameTwo,
    text="6",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button6isClicked
)
buttonSix.pack(side=LEFT, expand=True, fill="both")

buttonAdd = Button(
    frameTwo,
    text="+",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=buttonAddisClicked
)
buttonAdd.pack(side=LEFT, expand=True, fill="both")

buttonSeven = Button(
    frameThree,
    text="7",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button7isClicked
)
buttonSeven.pack(side=LEFT, expand=True, fill="both")

buttonEight = Button(
    frameThree,
    text="8",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button8isClicked
)
buttonEight.pack(side=LEFT, expand=True, fill="both")

buttonNine = Button(
    frameThree,
    text="9",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button9isClicked
)
buttonNine.pack(side=LEFT, expand=True, fill="both")

buttonSub = Button(
    frameThree,
    text="-",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=buttonSubisClicked
)
buttonSub.pack(side=LEFT, expand=True, fill="both")

buttonZero = Button(
    frameFour,
    text="0",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=button0isClicked
)
buttonZero.pack(side=LEFT, expand=True, fill="both")

buttonMul = Button(
    frameFour,
    text="*",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=buttonMulisClicked
)
buttonMul.pack(side=LEFT, expand=True, fill="both")

buttonDiv = Button(
    frameFour,
    text="/",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=buttonDivisClicked,
)
buttonDiv.pack(side=LEFT, expand=True, fill="both")

buttonEqual = Button(
    frameFour,
    text="=",
    font=("Cambria", 22),
    relief=GROOVE,
    border=0,
    command=res,
    bg = "#D0CFCF"
)
buttonEqual.pack(side=LEFT, expand=True, fill="both")


guiWindow.mainloop()