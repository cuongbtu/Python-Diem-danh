import csv
import cv2
import os
from tkinter import messagebox
from tkinter import simpledialog


def isMajor(s):
    if (s != 'CN' and s != 'AT' and s != 'KT' and s != 'VT' and s != 'QT' and
            s != 'PT' and s != 'TT' and s != 'DT'): return False
    return True


# hàm kiểm tra số
def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Hàm kiểm tra mã sinh viên
def isStudentCode(s):
    if len(s) != 10: return False
    if (s[0] != 'B'): return False
    if (s[3:5] != 'DC'): return False
    if (isMajor(s[5:7]) == False): return False
    if (isNumber(s[1]) == False or isNumber(s[2]) == False or isNumber(s[7]) == False or
            isNumber(s[8]) == False or isNumber(s[9]) == False): return False
    return True


def studentCodeError():
    return messagebox.showinfo('SC Error', 'Mã sinh viên không hợp lệ')


def nameError():
    return messagebox.showinfo('Name Error', 'Tên không hợp lệ')


# Hàm chụp ảnh khuôn mặt
def takeImages():
    while (True):
        sc = ("" + simpledialog.askstring("Add Studen Code", "Nhập mã sinh viên:")).strip().upper()
        if (isStudentCode(sc) == True):
            break
        else:
            studentCodeError()
    while (True):
        name = ("" + simpledialog.askstring("Add Student Name", "Nhập Tên sinh viên:")).strip()
        if (name.isalpha()):
            break
        else:
            nameError()

    id = 0
    with open('ID', 'r') as f:
        id = str(int(f.read()) + 1)
    with open('ID', 'w+') as f:
        f.write(str(id))

    cam = cv2.VideoCapture(0)
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0

    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Số mẫu tăng dần
            sampleNum = sampleNum + 1
            # Lưu khuôn mặt được chụp trong thư mục TrainingImage
            cv2.imwrite("TrainingImage" + os.sep + name + "." + id + '.' +
                        str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            # Hiển thị frame khuôn mặt nhận dạng được
            cv2.imshow('Camera', img)
        # Chờ 75 miliseconds
        if cv2.waitKey(75) & 0xFF == ord('q'):
            break
        # Dừng lại khi số mẫu lớn hơn 60
        elif sampleNum > 60:
            break
    cam.release()
    cv2.destroyAllWindows()
    # res = "Images Saved for ID : " + id + " Name : " + name
    # Lưu ID và name vào file StudentDetails.csv trong thư mục StudentDetails
    row = [id, sc, name]
    with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()