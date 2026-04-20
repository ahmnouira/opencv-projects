import cv2

base = cv2.imread("image.png")
patch = cv2.imread("crop_position_patch_2.jpg")

base_h, base_w, _ = base.shape

h, w = patch.shape[:2]

# print(h, w, base_h, base_w)

base[0:h, base_w - w : base_w + w] = patch

cv2.imwrite("simple_replace.png", base)
