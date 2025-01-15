import cv2
import matplotlib.pyplot as plt
img = cv2.imread('test2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
print(gray.shape)


plt.axis("off")
# Thay đổi kích thước theo tỷ lệ
scale_percent = 30  # Tỷ lệ 50%
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized_img = cv2.resize(gray, dim, interpolation=cv2.INTER_AREA)
canny = cv2.Canny(img, 100, 200)
# sobel = cv2.Sobel(resized_img, 100, 200)


plt.subplot(1, 3, 1)
plt.title("anh goc")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.imshow(img) # lech mau``
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Gray")
plt.imshow(gray, cmap='gray')
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Canny")
plt.imshow(canny, cmap='gray')
# plt.imshow(canny) # lech mau``
plt.axis("off")




plt.show()