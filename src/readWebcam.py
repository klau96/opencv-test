import numpy as np
import cv2 as cv
import os

dir = os.path.dirname(os.path.abspath(__file__))
# img = cv.imread("src/static/p5r-joker-allout.webp")
# cv.imshow("p5r allout attack", img)
# cv.waitKey(0)


def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)

    frame = cv.flip(frame, 1)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


# ==== Helper draw functions ====


def drawBlankRectangle():
    blank = np.zeros((500, 500, 3), dtype="uint8")
    cv.rectangle(blank, (150, 150), (350, 350), (255, 155, 0), 2)

    cv.imshow("Blank", blank)


def cv_grayscale(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("Gray", gray)
    return gray


def drawCannyEdges(img):
    canny = cv.Canny(img, 125, 175)
    cv.imshow("Canny Edges", canny)
    return canny


def drawBlueImage(img):
    blank = np.zeros(img.shape[:2], dtype="uint8")  # only the first 2 values of shape
    print(img.shape)


def cv_bitwise_and(img, img2):
    operation = cv.bitwise_and(img, img2)
    return operation


def drawCircle(img):
    circle = cv.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 200, 255, -1)
    cv.imshow("circle", circle)


# haar cascade
haar_path = os.path.join(dir, "haarcascade.xml")
haar_cascade = cv.CascadeClassifier(haar_path)


def detectFace(gray):
    # detect multi scale
    # — tweak parameters to change sensitivity to noise
    faces_coord = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    return faces_coord


def drawRectangleAtFace(img, faces_coord):
    for x, y, w, h in faces_coord:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)


capture = cv.VideoCapture(0)

isTrue, frame = capture.read()
resized_first_frame = rescaleFrame(frame=frame)
blank = np.zeros(resized_first_frame.shape[:2], dtype="uint8")


# MAIN
while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame=frame)
    gray = cv_grayscale(resized_frame)
    b, g, r = cv.split(resized_frame)
    blue_frame = cv.merge([b, blank, blank])

    canny = drawCannyEdges(resized_frame)
    cv.imshow("Blue", blue_frame)

    canny2bgr = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    cannyblue = cv_bitwise_and(blue_frame, canny2bgr)

    faces_coord = detectFace(gray)
    drawRectangleAtFace(cannyblue, faces_coord)
    cv.imshow("Canny Blue Face Detection", cannyblue)

    if cv.waitKey(20) & 0xFF == ord("q"):  # bitwise operation to only take first bits
        break

capture.release()
cv.destroyAllWindows()
