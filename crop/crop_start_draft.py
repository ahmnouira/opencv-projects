print(h, w)


size = min(h, w)
# size = 154
start_x = (w - size) // 2  # 214
start_y = (h - size) // 2  # 0


cropped_img = img[0:h, 0:size]


print(start_y, cropped_img.shape)
cv2.imwrite("crop_start.jpg", cropped_img)
