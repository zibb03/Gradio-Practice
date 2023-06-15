import yolov3
import cv2

import gradio as gr

description = "문장을 입력하면 긍정문인지, 부정문인지 판단합니다."
title = "긍정, 부정문 판독기"

def predict(img):
    model = yolov3.YOLO_V3()
    # path = '../YOLOv3/desk.jpg'

    # img = cv2.imread(path)
    model.build()
    model.load()
    result = model.predict(img)
    # cv2.imshow('result', result)
    # cv2.waitKey(0)

    return result

iface = gr.Interface(
    fn=predict,
    inputs='image',
    outputs='image',
    description=description,
    title=title,
    # examples=[["안녕하세요"]]
)

iface.launch(share=False)