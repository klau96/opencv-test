import cv2 as cv
import numpy as np

img = cv.imread("src/static/p5r-logo.png")

cv.imshow("img", img)


# apply gaussian blur to remove noise
def gaussianBlur(img, sigmas=(7, 7), border=0):
    gauss = cv.GaussianBlur(img, sigmas, border)
    cv.imshow("gaussian blur", gauss)
    return gauss


# laplacian
# apply laplacian operator to find gradients
def laplacian(gray):
    lap = cv.Laplacian(gray, cv.CV_64F)
    cv.imshow("laplacian", lap)
    return lap


# sobel x
# sobel y
# combined sobel
# bitwise_or — laplacian and combined sobel

while True:

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

# capture.release()
cv.destroyAllWindows()
