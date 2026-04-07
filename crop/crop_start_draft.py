import cv2

img = cv2.imread("image.jpg")
h, w, _ = img.shape

size = min(h, w)
# size = 154
start_x = (w - size) // 2  # 214
start_y = (h - size) // 2  # 0

cropped_img = img[0:h, 0:size]

cv2.imwrite("crop_start.jpg", cropped_img)
