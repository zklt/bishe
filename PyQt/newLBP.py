from numpy import *
from numpy import linalg as la
import cv2
import os
import math
import csv
import pickle
# from read_data import read_name_list
import CharacterWindow
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox


# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DIR = "D:/bishe/roi/"
if os.path.exists('ret'):
    os.remove('ret')
# 为了让LBP具有旋转不变性，将二进制串进行旋转。
# 假设一开始得到的LBP特征为10010000，那么将这个二进制特征，
# 按照顺时针方向旋转，可以转化为00001001的形式，这样得到的LBP值是最小的。
# 无论图像怎么旋转，对点提取的二进制特征的最小值是不变的，
# 用最小值作为提取的LBP特征，这样LBP就是旋转不变的了。
def minBinary(pixel):
    length = len(pixel)
    zero = ''
    for i in range(length)[::-1]:
        if pixel[i] == '0':
            pixel = pixel[:i]
            zero += '0'
        else:
            return zero + pixel
    if len(pixel) == 0:
        return '0'


# 加载图像
def loadImageSet(add):  # add是路径
    print("步骤1")
    FaceMat = mat(zeros((len(os.listdir(add)), 279 * 279)))  # 根据图片尺寸更改   一共有几行
    j = 0
    for i in os.listdir(add):
        # print(i)  #图片正常显示了
        # print(i.split('.')[1])  输出结果：jpg
        if i.split('.')[1] == 'jpg':
            try:
                img = cv2.imread(add + i, 0)
                # print(add+i)   输出结果：D:\opencv\huge/15138183801.jpg
                # cv2.imwrite(str(i)+'.jpg',img)
            except:
                print('load %s failed' % i)
            FaceMat[j, :] = mat(img).flatten()
            # print(FaceMat[j,:])   #取第j行
            # print(FaceMat[:,j])   #取第j列
            # http://blog.csdn.net/qq_18433441/article/details/54916991  flatten详解
            j += 1
    # print(FaceMat)
    return FaceMat


# 算法主过程
def LBP(FaceMat, R=2, P=8):
    print("步骤2")
    Region8_x = [-1, 0, 1, 1, 1, 0, -1, -1]
    Region8_y = [-1, -1, -1, 0, 1, 1, 1, 0]
    pi = math.pi
    LBPoperator = mat(zeros(shape(FaceMat)))
    for i in range(shape(FaceMat)[1]):
        # 对每一个图像进行处理  转化成116*98的二维矩阵
        face = FaceMat[:, i].reshape(279, 279)

        W, H = shape(face)
        tempface = mat(zeros((W, H)))
        for x in range(R, W - R):
            for y in range(R, H - R):
                repixel = ''
                pixel = int(face[x, y])  # 取每一个值
                # 　圆形LBP算子
                for p in [2, 1, 0, 7, 6, 5, 4, 3]:
                    p = float(p)
                    xp = x + R * cos(2 * pi * (p / P))
                    yp = y - R * sin(2 * pi * (p / P))
                    # print(xp)  输出结果 2.0
                    # print(pixel)  输出结果 1
                    # print(yp)   0.0
                    # print(face[2,0])  1.0
                    if int(face[int(xp), int(yp)]) > pixel:
                        repixel += '1'
                    else:
                        repixel += '0'
                # minBinary保持LBP算子旋转不变
                tempface[x, y] = int(minBinary(repixel), base=2)
        LBPoperator[:, i] = tempface.flatten().T
        # cv2.imwrite(str(i)+'hh.jpg',array(tempface,uint8))
    return LBPoperator

    # judgeImg:未知判断图像
    # LBPoperator:实验图像的LBP算子
    # exHistograms:实验图像的直方图分布


def judgePalm(judgeImg, LBPoperator, exHistograms):
    judgeImg = judgeImg.T
    ImgLBPope = LBP(judgeImg)
    #  把图片分为7*4份 , calHistogram返回的直方图矩阵有28个小矩阵内的直方图
    judgeHistogram = calHistogram(ImgLBPope)
    minIndex = 0
    minVals = inf  # 正无穷
    diff = inf
    ret = -1
    for i in range(shape(LBPoperator)[1]):
        exHistogram = exHistograms[:, i]
        diff_ = (array(exHistogram - judgeHistogram) ** 2).sum()
        if diff_ < diff and diff_ != 0:
            diff = diff_
            ret = i
    return diff, ret


# 统计直方图
def calHistogram(ImgLBPope):
    Img = ImgLBPope.reshape(279, 279)
    W, H = shape(Img)
    # 把图片分为7*4份
    Histogram = mat(zeros((256, 7 * 4)))
    maskx, masky = W / 4, H / 7  # 29 14
    for i in range(4):
        for j in range(7):
            # 使用掩膜opencv来获得子矩阵直方图
            mask = zeros(shape(Img), uint8)
            mask[int(i * maskx): int((i + 1) * maskx), int(j * masky):int((j + 1) * masky)] = 255
            hist = cv2.calcHist([array(Img, uint8)], [0], mask, [256], [0, 256])
            Histogram[:, (i + 1) * (j + 1) - 1] = mat(hist).flatten().T
    return Histogram.flatten().T


allLBPoperator = []
allexHistograms = []

allTuPianPath = 'D:/bishe/roi/'

def eachLBP(path:str):
    allLBPoperator = []
    allexHistograms = []
    FaceMat = loadImageSet(path).T  # 反转矩阵
    LBPoperator = LBP(FaceMat)  # 获得实验图像LBP算子

    # 获得实验图像的直方图分布，这里计算是为了可以多次使用
    exHistograms = mat(zeros((256 * 4 * 7, shape(LBPoperator)[1])))
    for i in range(shape(LBPoperator)[1]):
        exHistogram = calHistogram(LBPoperator[:, i])
        exHistograms[:, i] = exHistogram
    allLBPoperator.append(LBPoperator)
    allexHistograms.append(exHistograms)
    names = os.listdir(path)
    tmp = []
    for i in names:
        l = i.split(".")
        if l[-1] == 'jpg':
            tmp.append(i)
    names = tmp
    with open("allLBPoperator", "wb") as f:
        pickle.dump(allLBPoperator, f)
    with open("allexHistograms", "wb") as f:
        pickle.dump(allexHistograms, f)
    with open("names", "wb") as f:
        pickle.dump(names, f)

def runLBP(tuPianPath):
    roi = "D:/bishe/roi/"
    result = inf
    with open("allLBPoperator", "rb") as f:
        allLBPoperator = pickle.load(f)
    with open("allexHistograms", "rb") as f:
        allexHistograms = pickle.load(f)
    with open("names", "rb") as f:
        names = pickle.load(f)
    for file in os.listdir(roi):
        for i in range(len(allLBPoperator)):
            jresult, i = judgePalm(mat(cv2.imread(roi + file, 0)).flatten(), allLBPoperator[i], allexHistograms[i])
            print(file + '-->' + names[i])
            p = "方法:{0}   {1} 找到对应图片 {2}".format('LBP', file, names[i])
            print(p)
            with open("ret", "ab") as f:
                f.write(p.encode() + b'\n')


if __name__ == '__main__':
    allTuPianPath = 'D:/bishe/roi/'
    #eachLBP(allTuPianPath)
    runLBP(allTuPianPath)
