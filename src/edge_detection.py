import cv2 as cv
import numpy as np

img = cv.imread("src/static/p5r-logo.png")

cv.imshow("img", img)


# apply gaussian blur to remove noise
def gaussianBlur(img, sigmas=(7, 7), border=0):
    gauss = cv.GaussianBlur(img, sigmas, border)
    cv.imshow("gaussian blur", gauss)
    return gauss


# sobel x
# sobel y
# combined sobel (first derivative)
def combinedSobel(gray):
    sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
    # cv.imshow("Sobel X", sobelX)
    # cv.imshow("Sobel Y", sobelY)
    combined_sobel = cv.bitwise_or(sobelX, sobelY)
    cv.imshow("Combined Sobel", combined_sobel)

    return combined_sobel


# laplacian (second derivative)
# apply laplacian operator to find gradients
def laplacian(gray):
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv.imshow("laplacian", lap)
    return lap


capture = cv.VideoCapture(0)

gauss = gaussianBlur(img)
gray = cv.cvtColor(gauss, cv.COLOR_BGR2GRAY)

newgray = np.copy(gray)
lap = laplacian(gray)
csobel = combinedSobel(gray)

while True:
    isTrue, frame = capture.read()

    # gauss = gaussianBlur(frame)
    # gray = cv.cvtColor(gauss, cv.COLOR_BGR2GRAY)
    # lap = laplacian(gray)
    # combinedsobel = combinedSobel(gray)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break


capture.release()
# cv.destroyAllWindows()
