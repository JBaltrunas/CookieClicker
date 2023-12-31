import os.path
import tkinter as tk

# Vars
cookie_count = 0
finger_bonus = 0
granny_bonus = 0


# Functions
def get_finger_price():
    bonus = (3 ** finger_bonus) * 6
    return round(bonus, -len(str(bonus)) // 2)


def get_granny_price():
    bonus = (10 ** granny_bonus) * 1.5 + 15
    return int(round(bonus, -len(str(int(bonus))) // 2))


def get_finger_bonus():
    if finger_bonus > 0:
        return int(1.5 ** finger_bonus)
    return 0


def get_granny_bonus():
    if granny_bonus > 0:
        return int(2 ** granny_bonus)
    return 0


def reset_cookie_clicker():
    global cookie_count, finger_bonus, granny_bonus
    cookie_count = 0
    finger_bonus = 0
    granny_bonus = 0
    write_stats()
    update_ui()


def get_count_per_click():
    count = 1
    count += get_finger_bonus()
    count += get_granny_bonus()
    return count


def update_ui():
    cookie_count_label.config(text=f"{cookie_count} cookies")
    cookie_button.config(text=f"Cookie\n{get_count_per_click()}")
    finger_button.config(text=f"Reinforsed_index_finger\n"
                               f"Level: {read_stats()[1]}\n"
                               f"Price: {get_finger_price()}")
    granny_button.config(text=f"Granny\n"
                               f"Level: {read_stats()[2]}\n"
                               f"Price: {get_granny_price()}")


def on_cookie_button_click():
    global cookie_count
    cookie_count += get_count_per_click()
    update_ui()
    write_stats()


def on_finger_button_click():
    global finger_bonus, cookie_count
    if get_finger_price() > cookie_count:
        return
    cookie_count -= get_finger_price()
    finger_bonus += 1
    update_ui()
    write_stats()


def on_granny_button_click():
    global granny_bonus, cookie_count
    if get_granny_price() > cookie_count:
        return
    cookie_count -= get_granny_price()
    granny_bonus += 1
    update_ui()
    write_stats()


def read_stats():
    if not os.path.isfile("cookies.txt"):
        return 0
    f = open("cookies.txt", "r")
    stats = f.read().split('\n')
    count = int(stats[0])
    finger = int(stats[1])
    granny = int(stats[2])
    f.close()
    return count, finger, granny


def write_stats():
    f = open("cookies.txt", "w")
    f.write(str(cookie_count) + "\n")
    f.write(str(finger_bonus) + "\n")
    f.write(str(granny_bonus))
    f.close()


# UI
window = tk.Tk()
window.geometry("350x300")

cookie_count_label = tk.Label(window, text=f"{read_stats()[0]} cookies")
cookie_count_label.grid(row=0, column=0)

cookie_button = tk.Button(window, command=on_cookie_button_click, width=10, height=2)
cookie_button.grid(row=1, column=0, padx=0, pady=0)

reset_button = tk.Button(window, text=f"Reset_game", command=reset_cookie_clicker, width=10, height=2)
reset_button.grid(row=1, column=2, padx=100, pady=0)

finger_button = tk.Button(window, command=on_finger_button_click, width=20, height=3)
finger_button.grid(row=2, column=0, padx=5, pady=5)

granny_button = tk.Button(window, command=on_granny_button_click , width=20, height=3)
granny_button.grid(row=3, column=0, padx=5, pady=5)

once_bonus_button = tk.Button(window, width=20, height=3)
once_bonus_button.grid(row=2, column=1, padx=5, pady=5)

#Actions
cookie_count, finger_bonus, granny_bonus = read_stats()
update_ui()

window.mainloop()