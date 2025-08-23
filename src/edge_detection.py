import cv2 as cv
import numpy as np

img = cv.imread("src/static/p5r-logo.png")

cv.imshow("img", img)

# laplacian
# sobel x
# sobel y
# combined sobel
# bitwise_or — laplacian and combined sobel

while True:

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

# capture.release()
cv.destroyAllWindows()
