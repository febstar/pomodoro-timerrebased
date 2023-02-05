from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timerz = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timerz)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    else:
        timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timerz
    check = ""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f'0{count_sec}'
    if count_min <= 9:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timerz = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            check += "✔"
        check_marks.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imagespic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=imagespic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, highlightthickness=0, bg=YELLOW)
timer.grid(column=1, row=1)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()