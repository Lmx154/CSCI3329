import tkinter as tk

top = tk.Tk()
top.title("Image Display")
canvas_width = 1329
canvas_height = 872
c = tk.Canvas(top, bg='blue', height=canvas_height, width=canvas_width)
img = tk.PhotoImage(file='gnome.png')
c.create_image(canvas_width // 2, canvas_height // 2, image=img)
c.pack()
top.mainloop()