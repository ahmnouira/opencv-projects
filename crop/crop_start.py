import cv2
import shutil

FIX = False
NAME = "tab"  # "crop_start"
PREFIX = ""  # "_"
MOVE = True
FIX_ONLY_LAST = True
OUTPUT_ASSETS = "/Users/ahmnouira/Desktop/askwe/assets/tabs"

# the image in the root folder
img = cv2.imread("image.jpg")
h, w, _ = img.shape

nb_cols = 5
right_m = 5
top_m = 0
bottom_m = -6
left_m = 10
tile_w = w // nb_cols


for i in range(nb_cols):
    # small fixe for the first three ones
    if FIX and i < 3:
        crop = img[0:h, (i * tile_w) + right_m : ((i + 1) * tile_w) + left_m]

    elif FIX_ONLY_LAST and i == nb_cols - 1:
        crop = img[0 : h + bottom_m, i * tile_w : (i + 1) * tile_w]
    else:
        crop = img[0:h, i * tile_w : (i + 1) * tile_w]

    file = f"output/{NAME}{PREFIX}{i + 1}.jpg"
    cv2.imwrite(file, crop)
    if MOVE:
        shutil.copy(file, OUTPUT_ASSETS)
