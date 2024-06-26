import tkinter as tk
import tkinter.font as tkFont
def handle_click(event):
    kilo =float(entry1.get())
    label2['text'] = f"{kilo/1.6}", "mile"
    print("you have just clicked")



w = tk.Tk()
width = str(int(w.winfo_screenwidth()/2) -300)
height = str(int(w.winfo_screenheight()/2) -300)
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

w.geometry("600x600+"+width+"+"+height)
hello = (tk.Label(
    text="Hello, Luis",
    font=fontStyle))

hello.pack()

button1 = tk.Button(text="Calculator", width=20, height=2)
button1.place(x=215, y=300)
button1.bind("<Button-1>", handle_click)

w.mainloop()

