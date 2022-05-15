import cv2

def cameraOn():
# Thiết lập 1 vòng lặp vô hạn trong đó liên tục chụp và hiển thị khung hình với sự hỗ trợ của thư viện opencv-python
# Vòng lặp được kết thúc khi người dùng nhấp vào 1 phím cụ thể, ở đây là q

    # Khởi tạo đối tượng camera
    cam = cv2.VideoCapture(0)
    # Thiết lập vòng lặp
    while(True):
        #Chụp khung hình
        ret, frame  = cam.read()
        #Hiển thị khung hình
        cv2.imshow('Checking Camera', frame)
        #kết thúc vòng lặp bằng phím q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    #Đóng cửa sổ
    cv2.destroyAllWindows()