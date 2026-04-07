import cv2

img = cv2.imread("image.jpg")

h, w, _ = img.shape

size = min(h, w)
start_x = (w - size) // 2
start_y = (h - size) // 2

cropped_img = img[start_y : start_y + size, start_x : start_x + size]

cv2.imwrite("crop_auto_center.jpg", cropped_img)
