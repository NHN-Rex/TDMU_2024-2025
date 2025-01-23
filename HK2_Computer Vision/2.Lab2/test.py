import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
# Đọc hình ảnh
image = cv2.imread('visit1.png', cv2.IMREAD_GRAYSCALE)

# ham threshold se so sanh tung pixel voi nguong (thresh=220), neu pixel > nguong thi gan pixel = 1, nguoc lai gan = 0
ret, binary = cv2.threshold(image, thresh=220, maxval=1, type=cv2.THRESH_BINARY)

# Tạo kernel
kernel = np.ones((15, 15), np.uint8)
kerneld = np.ones((5, 5), np.uint8)

# Thực hiện Erosion
eroded_image = cv2.erode(binary, kernel, iterations=1)
# Thuc hien gian no
dilated_image = cv2.dilate(eroded_image, kerneld, iterations=1)

# Dem doi tuong
labeled_img, num_object = ndimage.label(dilated_image)

# Hiển thị hình ảnh
# cv2.imshow('Original Image', image)
# cv2.imshow('Eroded Image', eroded_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.figure(figsize=(12, 8))



plt.subplot(2, 2, 1)
plt.imshow(binary, cmap='gray')
plt.title("Binary Image")


plt.subplot(2, 2, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title("Eroded Image")

plt.subplot(2, 2, 3)
plt.imshow(dilated_image, cmap='gray')
plt.title("Dilated Image")

plt.subplot(2, 2, 4)
plt.imshow(labeled_img, cmap='gray')
plt.title(f"Count {num_object} In Image")

plt.show()