import cv2


def get_image_info(img="image.jpg", rows=2, cols=2):
    img = cv2.imread(img)
    h, w, _ = img.shape
    tile_w = w // cols
    tile_h = h // rows
    size = min(h, w)
    start_x = (w - size) // 2
    start_y = (h - size) // 2

    # TODO: maybe make a class

    return (img, tile_w, tile_h, cols, rows)
