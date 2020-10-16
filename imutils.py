import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def save_video(video_name="camera0_out.avi", video_show=True, save_end_frame=True):
    # 创建相机端口
    cap = cv.VideoCapture(0)
    # 创建一个VideoWeiter对象,用以保存相机内容
    fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D') # 定义编解码器
    camera0 = cv.VideoWriter(video_name, fourcc, 30.0, (640, 480))

    if not cap.isOpened():
        print("cannot open camera")
        exit()
    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv.CAP_PROP_FPS)
        if not ret:
            print("cannot receive frame!")
            break
        if video_show:
            cv.namedWindow("camera0")
            cv.imshow("camera0",frame)
        camera0.write(frame)
        if cv.waitKey(1) == 27:  # ESC
            if save_end_frame:
                cv.imwrite("camera0_end_frame.jpg", frame)
            break
    cap.release()
    camera0.release()
    cv.destroyAllWindows()
