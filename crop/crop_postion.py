import cv2

img = cv2.imread("image.png")

h, w, _ = img.shape
print(h, w, _)

start_y, start_x = 0, 0
y = 12
x = h


cropped_img = img[start_y:y, start_x:x]

cv2.imwrite("crop_position_patch.jpg", cropped_img)
