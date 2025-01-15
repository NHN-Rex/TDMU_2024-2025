import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

file_path = "download.png"

# chuyen thanh anh nhi phan
img = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

plt.figure(figsize=(10, 7))

#(99, 17) là kernel size, phải là số lẻ, kích thước càng lớn thì độ làm mờ càng cao. sigmaY mặc định = sigmaX, nếu sigma=0
# thư viện sẽ tự động tính sigma dựa theo kích thước kernel

img_blur = cv.GaussianBlur(img, ksize=(99, 17), sigmaX=0)
img_binary = cv.adaptiveThreshold(img_blur, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, 
                                  thresholdType=cv.THRESH_BINARY, blockSize=15, C=8)
img_canny = cv.Canny(img_binary, 100, 200) # thực hiện loop để chọn ra lower threshold và upper threshold thích hợp
img_canny = np.array(img_canny)

labeled_img, num_object = ndimage.label(img_binary)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("original_gray")

plt.subplot(2, 2, 2)
plt.imshow(img_blur, cmap='gray')

plt.title("blur")

plt.subplot(2, 2, 3)
plt.imshow(img_canny, cmap='gray')

plt.title("canny")

plt.subplot(2, 2, 4)
plt.imshow(labeled_img, cmap='gray')
plt.title(f"{num_object} object")

plt.show()
            
