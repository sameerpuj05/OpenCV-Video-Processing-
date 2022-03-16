import cv2
import numpy as np


# https://www.youtube.com/watch?v=Fchzk1lDt7Q - Reference Link
# https://www.timpoulsen.com/2018/getting-user-input-with-opencv-trackbars.html

# Step 1: Color Thresholding using HSV
def nothing(x):
    pass


# cap = cv2.VideoCapture('/Users/teja/Desktop/Smart Manufacturing/Major Project/Coil_Movement.mp4')
cap = cv2.imread('/Users/teja/Desktop/pcb.png')
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 255, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

while True:
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(cap, cap, mask=mask)

    # cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(100)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Step 2: Canny edge detection and Drawing Contours
cap2 = cv2.imread('')  # Read the image after thresholding


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(imgContour, contours, -1, (255, 0, 255), 1)
    count = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 15500 > area > 10000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 1)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 1)
            w = int(w / 2)
            h = int(h / 2)
            cv2.putText(imgContour, str(count), (x + w, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
            # cv2.putText(imgContour, "Area"+str(int(area)), (x + w, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
            count = count + 1


while True:
    imgBlur = cv2.GaussianBlur(cap2, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgContour = cap2.copy()

    imgCanny = cv2.Canny(imgGray, 77, 251)
    kernel = np.ones((1, 1))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgContour)

    cv2.imshow("Result", imgContour)
    key = cv2.waitKey()
    if key == 27:
        break
