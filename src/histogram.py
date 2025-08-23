import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("src/static/p5r-logo.png")

cv.imshow("logo", img)

# plt.ion()


def setup_plot():
    # show histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("bins")
    plt.ylabel("# of pixels")
    plt.xlim([0, 256])
    plt.ylim([0, 100])
    plt.show(block=False)


setup_plot()


def generateGrayHistogram(frame):
    # generate histogram with opencv
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale logo", gray)
    gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

    plt.plot(gray_hist)
    plt.draw()
    plt.pause(0.1)


capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    cv.imshow("capture frame", frame)
    generateGrayHistogram(frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
