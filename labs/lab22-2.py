import tkinter as tk
import tkinter.font as tkFont

def handle_click(event):
    kilo = float(entry1.get())
    miles = kilo / 1.6
    label2["text"] = f"{miles:.1f} miles"

w = tk.Tk()
w.title("Kilo to Mile")
w.configure(bg='blue')
w.geometry('600x600')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
label1 = tk.Label(text="Please input a value in Kilometer.", font=fontStyle, bg='blue', fg='white')
label1.place(x=100, y=100)
entry1 = tk.Entry(fg="blue", width=10, font=('Lucida Grande', 20))
entry1.place(x=240, y=200)
button1 = tk.Button(text="Calculate!", width=25, height=5, bg="white", fg="black")
button1.place(x=215, y=300)
button1.bind("<Button-1>", handle_click)
label2 = tk.Label(text="", font=fontStyle, bg='blue', fg='white')
label2.place(x=260, y=400)

w.mainloop()
