from detector import Detector, draw_boxes, count_file
import os
import cv2

VIDEO_FOLDER_DIR = "data/video/"
OUTPUT_FOLDER_DIR = "/home/huycn/Documents/School/Python/data/cut_face/video_face/"

def cut_images(img, boxes, path, name):
    name = name.split(".")[0]
    if type(boxes) == type(None):
        print("don't have any box to draw")
    else:
        a = 0
        for box in boxes:
            box = [int(i) for i in box]
            [x1, y1, x2, y2] = box

            cut_img = img[y1:y2, x1:x2]

            img_dir = '{}/{}.{}.jpg'.format(OUTPUT_FOLDER_DIR, name, a)
            print("imwrite", img_dir)

            
            os.makedirs(os.path.dirname(path), exist_ok=True)
            cv2.imwrite(img_dir, cut_img)
            a += 1

def main():
    list_video_dir = os.listdir(VIDEO_FOLDER_DIR)
    if len(list_video_dir) == 0:
        print("dont have any video in this dir")
        return

        
    model = Detector('tinyface')
    for name in list_video_dir:
        video_dir = VIDEO_FOLDER_DIR + name
        print(video_dir)
        cap = cv2.VideoCapture(video_dir)
        i = 0
        while True:
            _, frame = cap.read()
            if i % 60 == 0:
                boxes, scores = model.detect(frame)
                
                cut_images(frame, boxes, OUTPUT_FOLDER_DIR + name.split('.')[0], str(i))
            i += 1
if __name__ == "__main__":
    main()  