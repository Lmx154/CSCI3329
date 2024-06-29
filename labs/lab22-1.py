import tkinter as tk

w = tk.Tk()

window_width = 600
window_height = 600
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
w.geometry('600x600')
name = tk.Label(w, text="Luis", bg="lightblue", fg="darkblue", font=("system", 24))

name.place(x=275, y=275)
w.mainloop()