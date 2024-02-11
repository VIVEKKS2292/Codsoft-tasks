import tkinter as tk

root = tk.Tk()

# click function Code
global scvalueco
def click(event):
    text = event.widget.cget("text")
    print(text)

    if text == "=" and scvalue.get() == "":
        return
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            expression = scvalue.get()

            # Removed leading zeros, but kept at least one digit
            expression_without_zeros = expression.lstrip('0') if expression != '0' else expression
            try:
                # eval function handles all arithmetic operation
                value = eval(expression_without_zeros)
            except Exception as e:
                print(e)
                value = "Syntax Error"
        
        scvalue.set(value)
        screen.update()
        pass
    elif text == "C":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        pass

# GUI part
# setting the bound 
root.geometry("320x500")
root.maxsize(320,500)
root.minsize(320,500)
# title of the window
root.title("Calculator")
# icon
root.wm_iconbitmap("tkinterCalci/Windows_Calculator_icon.ico")

# Input Feild setup
scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill="x", ipadx=10, ipady=10)  # setting up the padding to the input fiels and extend on X when resized

# frame use 1
frame = tk.Frame(root, bg="grey")
frame.pack()

# buttons
for number in range(9,6,-1):
    button = tk.Button(frame, text=str(number),width=1,height=1, padx=30, pady=5, font="lucida 18 bold")
    button.bind("<Button-1>",click)
    button.pack(side="left",padx=5,pady=5)

# frame use 2
frame = tk.Frame(root, bg="grey")
frame.pack()
# buttons
for number in range(6,3,-1):
    button = tk.Button(frame, text=str(number),width=1,height=1, padx=30, pady=5, font="lucida 18 bold")
    button.bind("<Button-1>",click)
    button.pack(side="left",padx=5,pady=5)

# frame use 3
frame = tk.Frame(root, bg="grey")
frame.pack()
# buttons
for number in range(3,0,-1):
    button = tk.Button(frame, text=str(number),width=1,height=1, padx=30, pady=5, font="lucida 18 bold")
    button.bind("<Button-1>",click)
    button.pack(side="left",padx=5,pady=5)

# frame use 4
frame = tk.Frame(root, bg="grey")
frame.pack()
button = tk.Button(frame, text="0", width=1,height=1,padx=19.5, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text=".", width=1,height=1,padx=18, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text="/", width=1,height=1, padx=18, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text="%", width=1,height=1, padx=17.4, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
# frame use 5
frame = tk.Frame(root, bg="grey")
frame.pack()
# buttons
button = tk.Button(frame, text="+", width=1,height=1, padx=15, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text="-", width=1,height=1, padx=15, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text="*", width=1,height=1, padx=15, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
button = tk.Button(frame, text="=", width=1,height=1,padx=29, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)
# frame use 6
frame = tk.Frame(root, bg="grey")
frame.pack()
#buttons
button = tk.Button(frame, text="C", width=13,height=1,padx=34, pady=5, font="lucida 18 bold")
button.bind("<Button-1>",click)
button.pack(side="left",padx=5,pady=5)


root.mainloop()


