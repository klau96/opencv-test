import numpy as np
import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width, height)

    frame = cv.flip(frame, 1)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)

while True:

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
