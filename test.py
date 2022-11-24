import pathlib
import cv2
import os
from insightface.app import FaceAnalysis
import matplotlib.pyplot as plt
# from deepface import detectors

RTSP_URL = 'http://127.0.0.1:8080'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/hearcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# from cctv
# cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
# from local cam
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('Cannot open camera')
    exit(-1)


def detect_faces_cv2(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize = (30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces
def detect_faces_insightface(image):
    app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    faces = app.get(image)
    faces_bbox = [i['bbox'] for i in faces]
    print(faces_bbox)
    return faces_bbox

while True:
    _, frame = cap.read()

    # faces = detect_faces_insightface(frame)
    faces = detect_faces_cv2(frame)
    for (x, y, w, h) in faces:
        # print(x, y, w, h, frame.shape)
        # x = int(x)
        # y = int(y)
        # w = int(w)
        # h = int(h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    # cv2.imshow('RTSP stream', frame)
    imgplot = plt.imshow(frame)


cap.release()
cv2.destroyAllWindows()