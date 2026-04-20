import cv2

ROTATE = True

img = cv2.imread("image.png")

h, w, _ = img.shape
print(h, w, _)

start_y, start_x = 0, 0
x = h
y = 12

img = img[h - y : h + y, start_x:x]

if ROTATE:
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("crop_position_bottom_patch.jpg", img)
