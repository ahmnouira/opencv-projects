import cv2

img = cv2.imread("image.png")

h, w, _ = img.shape
print(h, w, _)

start_y, start_x = 0, 0
y = h
# x = 20
x = 12


cropped_img = img[start_y:y, start_x:x]

cv2.imwrite("crop_position_patch_2.jpg", cropped_img)
