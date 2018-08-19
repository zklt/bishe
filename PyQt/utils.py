import cv2, imutils as im, argparse
import numpy as np
import math
import time

def process_image(img):
    CORRECTION_NEEDED = False
    # Define lower and upper bounds of skin areas in YCrCb colour space.
    lower = np.array([0, 139, 60], np.uint8)
    upper = np.array([255, 180, 127], np.uint8)
    # convert img into 300*x large
    r = 300.0 / img.shape[1]
    dim = (300, int(img.shape[0] * r))
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    original = img.copy()

    # Extract skin areas from the image and apply thresholding
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

    mask = cv2.inRange(ycrcb, lower, upper)
    skin = cv2.bitwise_and(ycrcb, ycrcb, mask=mask)
    _, black_and_white = cv2.threshold(mask, 127, 255, 0)

    # Find contours from the thresholded image
    _, contours, _ = cv2.findContours(black_and_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get the maximum contour. It is usually the hand.
    length = len(contours)
    maxArea = -1
    final_Contour = np.zeros(img.shape, np.uint8)
    # print(final_Contour)
    if length > 0:
        for i in range(length):
            temp = contours[i]
            area = cv2.contourArea(temp)
            if area > maxArea:
                maxArea = area
                ci = i
        largest_contour = contours[ci]

    # print(largest_contour)
    # Draw it on the image, in case you need to see the ellipse.
    cv2.drawContours(final_Contour, [largest_contour], 0, (0, 255, 0), 2)

    # Get the angle of inclination
    ellipse = _, _, angle = cv2.fitEllipse(largest_contour)

    # original = cv2.bitwise_and(original, original, mask=black_and_white)

    # Vertical adjustment correction
    '''
    This variable is used when the result of hand segmentation is upside down. Will change it to 0 or 180 to correct the actual angle.
    The issue arises because the angle is returned only between 0 and 180, rather than 360.
    '''
    vertical_adjustment_correction = 0
    if CORRECTION_NEEDED: vertical_adjustment_correction = 180

    # Rotate the image to get hand upright
    if angle >= 90:
        black_and_white = im.rotate_bound(black_and_white, vertical_adjustment_correction + 180 - angle)
        original = im.rotate_bound(original, vertical_adjustment_correction + 180 - angle)
        final_Contour = im.rotate_bound(original, vertical_adjustment_correction + 180 - angle)
    else:
        black_and_white = im.rotate_bound(black_and_white, vertical_adjustment_correction - angle)
        original = im.rotate_bound(original, vertical_adjustment_correction - angle)
        final_Contour = im.rotate_bound(final_Contour, vertical_adjustment_correction - angle)

    original = cv2.bitwise_and(original, original, mask=black_and_white)
    # cv2.imshow('Extracted Hand', final_Contour)
    #cv2.imshow('Original image', original)

    # 求手掌中心
    # 参考至http://answers.opencv.org/question/180668/how-to-find-the-center-of-one-palm-in-the-picture/
    # 因为已经是黑白的，所以省略这一句
    # cv2.threshold(black_and_white, black_and_white, 200, 255, cv2.THRESH_BINARY)

    distance = cv2.distanceTransform(black_and_white, cv2.DIST_L2, 5, cv2.CV_32F)
    # Calculates the distance to the closest zero pixel for each pixel of the source image.
    maxdist = 0
    # rows,cols = img.shape
    for i in range(distance.shape[0]):
        for j in range(distance.shape[1]):
            # 先扩展一下访问像素的 .at 的用法：
            # cv::mat的成员函数： .at(int y， int x)
            # 可以用来存取图像中对应坐标为（x，y）的元素坐标。
            # 但是在使用它时要注意，在编译期必须要已知图像的数据类型.
            # 这是因为cv::mat可以存放任意数据类型的元素。因此at方法的实现是用模板函数来实现的。
            dist = distance[i][j]
            if maxdist < dist:
                x = j
                y = i
                maxdist = dist
    # 得到手掌中心并画出最大内切圆
    final_img = original.copy()
    cv2.circle(original, (x, y), maxdist, (255, 100, 255), 1, 8, 0)
    half_slide = maxdist * math.cos(math.pi / 4)
    (left, right, top, bottom) = ((x - half_slide), (x + half_slide), (y - half_slide), (y + half_slide))
    p1 = (int(left), int(top))
    p2 = (int(right), int(bottom))
    cv2.rectangle(original, p1, p2, (77, 255, 9), 1, 1)
    final_img = img[int(top):int(bottom),int(left):int(right)]
    # cv2.imshow('palm image', original)
    return final_img

def cacSIFTFeatureAndCompare(srcImage1: np.ndarray, srcImage2: np.ndarray):
    if srcImage1 is None or srcImage2 is None:
        return
    grayMat1 = srcImage1
    cv2.normalize(grayMat1, grayMat1, 0, 255, cv2.NORM_MINMAX)
    grayMat2 = srcImage2
    cv2.normalize(grayMat2, grayMat2, 0, 255, cv2.NORM_MINMAX)
    sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.02, sigma=1)

    keypoints1, descriptors1 = sift.detectAndCompute(grayMat1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(grayMat2, None)

    result = 0
    k1, k2 = keypoints1, keypoints2
    d1, d2 = descriptors1, descriptors2
    if len(k1) > 0 and len(k2) > 0:
        matcher = cv2.BFMatcher_create(cv2.NORM_L2)
        viewMatches = []
        matches = matcher.match(d1, d2)
        minDist = 1000
        for i in matches:
            if i.distance < minDist:
                minDist = i.distance
        num = 0
        print("minDist:", minDist)
        for i in matches:
            if i.distance <= 2 * minDist:
                result += i.distance * i.distance
                viewMatches.append(i)
                num += 1
        if num < len(matches) * 0.01:
            return 1 << 32
        result = float(result) / float(num)
        return result

def cacSURFFeatureAndCompare(srcImage1: np.ndarray, srcImage2: np.ndarray, para: float):
    if srcImage1 is None or srcImage2 is None:
        return
    grayMat1 = srcImage1
    grayMat2 = srcImage2
    # cv2.imshow("" ,grayMat1)
    # cv2.waitKey()
    surf = cv2.xfeatures2d_SURF.create(para)
    k1, d1 = surf.detectAndCompute(grayMat1, None)
    k2, d2 = surf.detectAndCompute(grayMat2, None)
    result = 0
    if len(k1) > 0 and len(k2) > 0:
        matcher = cv2.FlannBasedMatcher.create()
        viewMatches = []
        matches = matcher.match(d1, d2)
        minDist = 100
        for i in matches:
            if i.distance < minDist:
                minDist = i.distance
        num = 0
        print("minDist:", minDist)
        for i in matches:
            if i.distance <= 2 * minDist:
                result += i.distance * i.distance
                viewMatches.append(i)
                num += 1
        if num < len(matches) * 0.01:
            return 1 << 32
        result = float(result) / float(num)
        return result


def cacORBFeatureSAndCompare(srcImage1: np.ndarray, srcImage2: np.ndarray):
    if srcImage1 is None or srcImage2 is None:
        return
    orb = cv2.ORB_create()
    if not isinstance(orb, cv2.ORB): return
    orb.setFastThreshold(3)
    orb.setScaleFactor(1.3)
    orb.setNLevels(16)
    orb.setEdgeThreshold(3)
    keyPoint1, descriptorMat1 = orb.detectAndCompute(srcImage1, None)
    keyPoint2, descriptorMat2 = orb.detectAndCompute(srcImage2, None)
    result = 0
    k1, k2 = keyPoint1, keyPoint2
    d1, d2 = descriptorMat1, descriptorMat2
    if len(k1) > 0 and len(k2) > 0:
        matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
        viewMatches = []
        matches = matcher.match(d1, d2)
        minDist = 200
        for i in matches:
            if i.distance < minDist:
                minDist = i.distance
        num = 0
        print("minDist:", minDist)
        for i in matches:
            result += i.distance
            viewMatches.append(i)
            num += 1
        # if num < len(matches) * 0.01:
        #     print("inf")
        #     return 1 << 32
        result = float(result) / float(num)
        print(result)
        end = time.time()

        return result

def heqConvert(srcImage: np.ndarray):
    if srcImage is None:
        return

    BGR_plane = cv2.split(srcImage)
    for i in range(len(BGR_plane)):
        BGR_plane[i] = cv2.equalizeHist(BGR_plane[i])
    colorHeqImage = cv2.merge(BGR_plane)
    return colorHeqImage

def hand2(srcImage: np.ndarray):
        src_YCrCb = cv2.cvtColor(srcImage, cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(src_YCrCb)
        gray = channels[1]
        retval, binaryImage = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        iopen = cv2.morphologyEx(binaryImage, cv2.MORPH_OPEN, kernel)
        _, contours, hierarchy = cv2.findContours(iopen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        areas = np.zeros(len(contours))
        idx = 0
        for cont in contours:
            areas[idx] = cv2.contourArea(cont)
            idx += 1
        areas_s = cv2.sortIdx(areas, cv2.SORT_DESCENDING | cv2.SORT_EVERY_COLUMN)

        if not isinstance(areas_s, np.ndarray):
            return
        idx = areas_s[0]
        for i in areas_s:
            if areas[i] > areas[idx]:
                idx = i
        maxArea = areas[idx]
        poly_img = np.zeros(iopen.shape, np.uint8)
        cv2.drawContours(poly_img, contours, idx, [255, 255, 255], -1)
        img = cv2.bitwise_and(srcImage, srcImage, mask=poly_img)

        distance = cv2.distanceTransform(poly_img, cv2.DIST_L2, 5, cv2.CV_32F)
        # Calculates the distance to the closest zero pixel for each pixel of the source image.
        maxdist = 0
        # rows,cols = img.shape
        for i in range(distance.shape[0]):
            for j in range(distance.shape[1]):
                # 先扩展一下访问像素的 .at 的用法：
                # cv::mat的成员函数： .at(int y， int x)
                # 可以用来存取图像中对应坐标为（x，y）的元素坐标。
                # 但是在使用它时要注意，在编译期必须要已知图像的数据类型.
                # 这是因为cv::mat可以存放任意数据类型的元素。因此at方法的实现是用模板函数来实现的。
                dist = distance[i][j]
                if maxdist < dist:
                    x = j
                    y = i
                    maxdist = dist

        # 得到手掌中心并画出最大内切圆
        final_img = img.copy()
        cv2.circle(img, (x+22, y-20), maxdist, (255, 100, 255), 1, 8, 0)
        half_slide = maxdist * math.cos(math.pi / 4)
        (left, right, top, bottom) = ((x+22 - half_slide), (x+22 + half_slide), (y-20 - half_slide), (y-20 + half_slide))
        p1 = (int(left), int(top))
        p2 = (int(right), int(bottom))
        cv2.rectangle(img, p1, p2, (77, 255, 9), 1, 1)
        final_img = img[int(top):int(bottom), int(left):int(right)]
        # final_img = cv2.cvtColor(final_img, cv2.COLOR_BGRA2GRAY)
        return final_img

if __name__ == '__main__':
    i = cv2.imread("./Images/1.jpg", 0)
    cacSURFFeatureAndCompare(i,i,1000)