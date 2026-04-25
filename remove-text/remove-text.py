import cv2
import pytesseract


def check_old():
    if not data or all(x == "" for x in text):
        # print("Empty pass")
        pass

    elif text == ["", "", "", "", "Ahmed"]:
        # print("Empty pass only Ahmed array")
        pass


video_path = "input.mp4"
output_path = "output.mp4"

cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, 25, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect text boxes
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    text = data["text"]
    text_data = []

    for t in text:
        if not t:
            continue
        text_data.append(t)

    if text_data and text_data != ["Ahmed"]:
        print(text_data)

        for i in range(len(text_data)):
            x, y, w, h = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            if int(data["conf"][i]) > 60:
                roi = frame[y : y + h, x : x + w]
                print("roi", roi)
                try:
                    blur = cv2.GaussianBlur(roi, (23, 23), 30)
                except Exception as e:
                    print(e)
                    continue

                frame[y : y + h, x : x + w] = blur

    out.write(frame)

cap.release()
out.release()
