import numpy as np
import cv2 as cv

# img = cv.imread("src/static/p5r-joker-allout.webp")

# cv.imshow("p5r allout attack", img)

# cv.waitKey(0)


def drawBlank():
    blank = np.zeros((500, 500, 3), dtype="uint8")
    cv.rectangle(blank, (150, 150), (350, 350), (0, 155, 255), 2)

    cv.imshow("Blank", blank)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


drawBlank()

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame=frame)

    # cv.imshow("MacOS Webcam", frame)
    cv.imshow("Macos Webcam resized", resized_frame)

    if cv.waitKey(20) & 0xFF == ord("d"):  # bitwise operation to only take first bits
        break

capture.release()
cv.destroyAllWindows()
