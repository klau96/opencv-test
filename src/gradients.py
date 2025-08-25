import cv2 as cv
import numpy as np

img = cv.imread("src/static/p5r-logo.png")
cv.imshow("first image", img)


# apply gaussian blur to remove noise
def gaussianBlur(img, sigmas=(7, 7), border=0):
    gauss = cv.GaussianBlur(img, sigmas, border)
    cv.imshow("gaussian blur", gauss)
    return gauss


# apply laplacian operator to find gradients
def laplacian(gray):
    lap = cv.Laplacian(gray, cv.CV_64F)
    cv.imshow("laplacian", lap)
    return lap


gauss = gaussianBlur(img, sigmas=(3, 3))
gray = cv.cvtColor()

while True:
    laplacian(img)
    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
