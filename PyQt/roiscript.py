import utils
import os
import cv2

if __name__ == '__main__':
    resize = "./Images/resize/test/"
    roi = "./Images/testroi/"
    for root,dirs,files in os.walk(resize):
        for file in files:
            img = cv2.imread(resize + file)
            if img is None:
                print(file, "is None")
                continue
            try:
                img = utils.hand2(img)
                img = cv2.resize(img, (279, 279), interpolation=cv2.INTER_CUBIC)
            except OverflowError as e:
                print(e)
                continue
            if os.path.exists(roi + file):
                os.remove(roi + file)
            newname = roi + file
            cv2.imwrite(newname, img)
