from tokenize import Number
import cv2
import os
from PIL import Image, ImageDraw
import torch
from facenet_pytorch import MTCNN
from dotenv import load_dotenv
import dotenv
import sys
from retinaface import RetinaFace

class Detector:
    def __init__(self, name) -> None:
        self.name = name
        if name == "mtcnn":
            device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
            self.model = MTCNN(keep_all=True, device=device)
        elif name == "cascade":
            self.model = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        else: 
            self.model = RetinaFace
        print("detector: ", self.name)
    def detect(self, image):
        if self.name == "mtcnn":
            boxes, scores = self.model.detect(image)
        elif self.name == "cascade":
            pass
        else: 
            resp = self.model.detect_faces(image)
            if type(resp) is tuple:
                print("No any face in this image: ")
                return [], []
            boxes = []
            scores = []
            for i in resp:
                boxes.append(resp[i]["facial_area"])
                scores.append(resp[i]["score"])
        return boxes, scores

def draw_boxes(img, boxes):
    if type(boxes) == type(None):
        print("don't have any box to draw")
    else:
        for box in boxes:
            box = [int(i) for i in box]
            [x1, y1, x2, y2] = box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
    return img
def count_file(dir):
    count = 0
    for path in os.listdir(dir):
        count += 1
    return count