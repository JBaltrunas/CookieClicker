import os.path
import tkinter as tk

# Vars
cookie_count = 0


# Functions
def on_cookie_button_click():
    global cookie_count
    cookie_count += 1
    cookie_count_label.config(text=f"{cookie_count} cookies")
    write_cookie_count()


def read_cookie_count():
    if not os.path.isfile("cookies.txt"):
        return 0
    f = open("cookies.txt", "r")
    res = int(f.read())
    f.close()
    return res


def write_cookie_count():
    f = open("cookies.txt", "w")
    f.write(str(cookie_count))
    f.close()


# UI
window = tk.Tk()
window.geometry("200x300")

cookie_count_label = tk.Label(window, text=f"{read_cookie_count()} cookies")
cookie_count_label.grid(row=0, column=0)

cookie_button = tk.Button(window, text="Cookie", command=on_cookie_button_click, width=10, height=2)
cookie_button.grid(row=1, column=0, padx=10, pady=0)


#Actions
cookie_count = read_cookie_count()

window.mainloop()