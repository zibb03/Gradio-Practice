import cv2
import gradio as gr

description = "사진을 첨부하면 사진 속 얼굴의 위치를 표시합니다."
title = "Face Detection"

def predict(img):
    # cascade xml 파일 선택
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # img = cv2.imread('face.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    if len(faces):
        for (x, y, w, h) in faces:
            face_rectangle = cv2.rectangle(
                img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            Face_text = cv2.putText(img=face_rectangle,
                                    text="Face",
                                    org=(x, y + h + 30),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1, color=(0, 0, 255),
                                    thickness=2, lineType=cv2.LINE_4)

    # cv2.imshow("image", img)
    # cv2.waitKey(0)

    return img

iface = gr.Interface(
    fn=predict,
    inputs='image',
    outputs='image',
    description=description,
    title=title,
)

iface.launch(share=False)