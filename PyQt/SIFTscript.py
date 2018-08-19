import os
import utils
import CharacterWindow
import cv2
import time

DIR = "./Images/roi/"
if os.path.exists('ret1'):
    os.remove('ret1')
class Script:
    def __repr__(self):
        return self.readImageName


    def __init__(self, path:str):
        p = path.strip('/')
        a = p.split("/")
        self.readImageName = a[-1]
        self.files = os.listdir(DIR)
        find = False
        for i in reversed(range(len(self.files))):
            if self.files[i] == self.readImageName:
                del self.files[i]
                find = True
                break
        if not find:
            print("在{0}里没有找到与{1}同名文件".format(DIR, self.readImageName))
        self.__readImage = cv2.imread(path, 0)
        if self.__readImage is None:
            raise FileNotFoundError("{0} 图片没有找到".format(path))

    def orb(self, img):
        src1 = self.__readImage
        # img = cv2.Canny(img, 40, 50)
        # src1 = cv2.Canny(src1, 40, 50)
        return utils.cacORBFeatureSAndCompare(src1, img)

    def sift(self, img):
        src1 = self.__readImage
        return utils.cacSIFTFeatureAndCompare(src1, img)

    def surf(self, img):
        src1 = self.__readImage
        return utils.cacSURFFeatureAndCompare(src1, img, 5)

    def run(self, type):
        def ret():
            files = self.files
            if type == "orb":
                f = self.orb
            elif type == "sift":
                f = self.sift
            elif type == "surf":
                f = self.surf
            res = 99999999
            name = None
            for i in files:
                img = cv2.imread(DIR + i, 0)
                # img = utils.hand2(img)
                # cv2.imwrite("pipei.jpg", img)
                # img = cv2.imread("pipei.jpg")

                res_ = f(img)
                print("图片名字:{0}".format(i))
                res_ = res_ if res_ is not None else 9999999
                name = name if res_ > res else i
                res = res if res_ > res else res_
            if name is None:
                p = "方法:{0}   {1} 没有找到对应的图片".format(f.__name__, self.readImageName)
                print("方法:{0}   {1} 没有找到对应的图片".format(f.__name__, self.readImageName))
                with open("ret1", "ab") as f:
                    f.write(p.encode() + b'\n')
            else:
                p = "方法:{0}   {1} 找到对应图片 {2}".format(f.__name__, self.readImageName, name)
                print(p)
                with open("ret1", "ab") as f:
                    f.write(p.encode() + b'\n')
            return name

        return ret
def U(a:str, b:str):
    a = a.split(".")[0].rstrip('1234567890')
    b = b.split('.')[0].rstrip('1234567890')
    return 1 if a == b else 0

if __name__ == '__main__':
    roi = DIR
    roi = roi.rstrip("/") + "/"
    res1 = 0
    t1 = time.time()
    for i in os.listdir(roi):
        s = Script(roi + i)
        j = s.run("orb")()
        res1 += U(i, j)
    t1 = time.time() - t1
    res2 = 0
    t2 = time.time()
    for i in os.listdir(roi):
        s = Script(roi + i)
        j = s.run("surf")()
        res2 += U(i, j)
    t2 = time.time() - t2
    res3 = 0
    t3 = time.time()
    for i in os.listdir(roi):
        s = Script(roi + i)
        j = s.run("sift")()
        res3 += U(i, j)
    t3 = time.time() - t3
    with open('ret1', 'ab') as f:
        f.write("orb: {0} time: {1}\n".format(res1 / len(os.listdir(roi)), t1).encode())
        f.write("surf: {0} time: {1}\n".format(res2 / len(os.listdir(roi)), t2).encode())
        f.write("sift: {0} time: {1}\n".format(res3 / len(os.listdir(roi)), t3).encode())