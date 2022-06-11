Kode program : # import library python package
import cv2
import numpy as np

# membaca file gambar upin ipin.png yang berada dalam folder  yang sama dengan file
image = cv2.imread("upin ipin.png")

# menampilkan data piksel citra
print('Image', image)

# menampilkan citra original
cv2.imshow("citra Original", image)

# menampilkan citra grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# menampilkan citra HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Picture", hsv)

# median Filter
img_median = cv2.medianBlur(hsv, 5)  # menambahkan median filter ke image
cv2.imshow('Median Filter 0', img_median)

# Applying otau in Green channel
img = img_median[:, :, 1]
th, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("otau Tresholding", th)

# opening
kernel = np.ones((7, 7), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)

# aritmatic and operation
dest_and = cv2.bitwise_and(image, image, mask=opening)
cv2.imshow('bitwase and', dest_and)

cv2.waitKey(0)
cv2.destroyAllWindows()
