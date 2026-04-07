import cv2

img = cv2.imread("image.jpg")


h, w, _ = img.shape

rows, cols = 2, 2  # change grid size (e.g, 3x3)

tile_h = h // rows
tile_w = w // cols

count = 0

for i in range(rows):
    for j in range(cols):
        crop = img[i * tile_h : (i + 1) * tile_h, j * tile_w : (j + 1) * tile_w]
        cv2.imwrite(f"cropped_img_{count}.jpg", crop)
        count += 1
