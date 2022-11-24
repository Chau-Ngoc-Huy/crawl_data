from detector import Detector, draw_boxes, count_file
import os
import cv2
import time

model = Detector('tinyface')

size = "medium"
input_path = "data/crawl_data/{}/".format(size)
output_path = "data/cut_face/{}/".format(size)

# img = cv2.imread("cam_1_background.png")
# cv2.imshow("image", img)
# cv2.waitKey(0)
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

            os.makedirs(os.path.dirname(path), exist_ok=True)
            cv2.imwrite('{}/{}.{}.jpg'.format(path, name, a), cut_img)
            a += 1

def show_images(imgs):
    for img in imgs:
        cv2.imshow("image", img)
        time.sleep(1000)

def main():
    for folder_name in os.listdir(input_path):
        folder_path= input_path + folder_name + '/'
        for img_name in os.listdir(folder_path):
            img_path = folder_path + img_name
            try:
                img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                boxes, scores = model.detect(img)
                print('detected image: ', img_path)

                # _img = draw_boxes(img, boxes)
                # cv2.imshow('img', _img)
                # cv2.waitKey(0)
                if (len(boxes) != 0):
                    imgs = cut_images(img, boxes, output_path + '{}/'.format(folder_name), img_name)
                    # print(imgs)
                else:
                    print("No any face in the image: ", img_name)
            except ValueError:
                print("Error: cant read this image")

    
if __name__ == "__main__":
    main()


