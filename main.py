import tkinter as tk


def click():
    global x
    x += 1
    label.config(text=f"{x} cookies")


x = 0
window = tk.Tk()
window.geometry("200x300")
#window.attributes("-fullscreen", True)

label = tk.Label(window, text="0 cookies")
label.grid(row=0, column=0, pady=50, padx=600)

button = tk.Button(window, text="Cookie", command=click, width=10, height=2)
#button.pack(fill=tk.BOTH, expand=True)
button.grid(row=1, column=0, padx=10, pady=0)

window.mainloop()