import tkinter
from PIL import ImageTk
from CheckCamera import *
from CaptureImage import *
from TrainImage import *
from Recognize import *

def selection(k):
    if k == 1: cameraOn()
    elif k == 2:
        takeImages()
        trainImages()
    elif k == 3:
        recognizeAttendence()

window = tkinter.Tk()
window.title("Attendance")
# Căn chỉnh màn hình
w_width, w_height = 820, 513
s_width, s_height = window.winfo_screenwidth(), window.winfo_screenheight()
x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
window.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))

icon = ImageTk.PhotoImage(Image.open("icon.jpg"))
window.iconphoto(True, icon)
f1 = tkinter.Frame(window)
f1.grid(row=0, column=0, sticky='news')
img = ImageTk.PhotoImage(Image.open("background.jpg"))
label = tkinter.Label(f1, image=img)
label.pack()

button1 = tkinter.Button(f1, text="Kiểm tra Camera", font=(
    "Consolas", 20), command=lambda : selection(1), fg='black', bg='pink', height = 1, width = 16)
button1.place(x=300, y=170)

button2 = tkinter.Button(f1, text="Thêm sinh viên", font=(
    "Consolas", 20), command=lambda : selection(2), fg='black', bg='pink', height = 1, width = 16)
button2.place(x=300, y=250)

button3 = tkinter.Button(f1, text="Điểm danh", font=(
    "Consolas", 20), command=lambda : selection(3), fg='black', bg='pink', height = 1, width = 16)
button3.place(x=300, y=330)

window.mainloop()