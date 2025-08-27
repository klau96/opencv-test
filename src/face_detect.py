import os
import cv2 as cv
import numpy as np


dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(dir, ".", "static", "mark_interview.jpg")
img = cv.imread(img_path)


# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# haar cascade
haar_path = os.path.join(dir, "haarcascade.xml")
haar_cascade = cv.CascadeClassifier(haar_path)

# detect multi scale
# — tweak parameters to change sensitivity to noise
faces_coord = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"face is at coord: {faces_coord}")

for x, y, w, h in faces_coord:
    cv.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), thickness=2)

cv.imshow("Gray face", gray)
cv.imshow("mark face detect", img)


def whileLoop():
    while True:
        if cv.waitKey(20) & 0xFF == ord("q"):
            break


whileLoop()

cv.destroyAllWindows()
