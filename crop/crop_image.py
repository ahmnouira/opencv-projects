import cv2

img = cv2.imread("image.jpg")

print(img.shape)


h, w, _ = img.shape

rows, cols = 2, 2

tile_h = h // rows
tile_w = w // cols

for row in range(rows):
    for col in range(cols):
        y = row * tile_h
        x = col * tile_w
        cropped_img = img[y : y + tile_h, x : x + tile_w]
        cv2.imwrite(f"cropped_img_{row}_{col}.jpg", cropped_img)
