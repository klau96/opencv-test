import numpy as np
import cv2 as cv

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


def drawBlank():
    blank = np.zeros((500, 500, 3), dtype="uint8")
    cv.rectangle(blank, (150, 150), (350, 350), (255, 155, 0), 2)

    cv.imshow("Blank", blank)


def drawGrayscale(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)


def drawCannyEdges(img):
    canny = cv.Canny(img, 125, 175)
    cv.imshow("Canny Edges", canny)


drawBlank()

capture = cv.VideoCapture(0)

# main
while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame=frame)

    # cv.imshow("MacOS Webcam", frame)
    # cv.imshow("Macos Webcam resized", resized_frame)
    drawCannyEdges(resized_frame)

    if cv.waitKey(20) & 0xFF == ord("q"):  # bitwise operation to only take first bits
        break

capture.release()
cv.destroyAllWindows()
