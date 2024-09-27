from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c" #short br
RED = "#e7305b" #long br
GREEN = "#9bdeac" #work
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        # count_down(LONG_BREAK_MIN * 60)
        count_down(8)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # count_down(SHORT_BREAK_MIN * 60)
        count_down(1)
        title_label.config(text="Break", fg=PINK)
    else:
        # count_down(WORK_MIN * 60)
        count_down(3)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):


    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        work_sessions = math.floor(reps/2)
        check_marks.config(text="✓" * work_sessions)
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #size of the image 200x224
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img) #create and center img
timer_text = canvas.create_text(100, 130, text="00:00", fill = "white", font = (FONT_NAME, 35, "bold")) #create and center text
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", bg=YELLOW,fg=GREEN, font = (FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

check_marks = Label(bg=YELLOW,fg=GREEN, font = (FONT_NAME, 25, "bold"))
check_marks.grid(column=1, row=3)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

mainloop()