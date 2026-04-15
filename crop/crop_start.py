import cv2

# the image in the root folder
img = cv2.imread("image.jpg")
h, w, _ = img.shape

nb_cols = 5
right_m = 5
left_m = 10
FIX = False
NAME = "tab"  # "crop_start"
PREFIX = ""  # "_"

tile_w = w // nb_cols


for i in range(nb_cols):
    # small fixe for the first three ones
    if FIX and i < 3:
        crop = img[0:h, (i * tile_w) + right_m : ((i + 1) * tile_w) + left_m]
    else:
        crop = img[0:h, i * tile_w : (i + 1) * tile_w]
    cv2.imwrite(f"output/{NAME}{PREFIX}{i + 1}.jpg", crop)
