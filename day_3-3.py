import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 그림 파일 불러오기
img = cv.imread('images.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# 이진화 수행하기
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 2)
thresh3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)

# 그림별 제목 정하기
titles = ['origin', 'global thresholding(v = 127)', 'adaptive mean thresholding', 'adaptive gaussian thresholding']

# 동시에 여러 그림 출력하기
images = [img, thresh1, thresh2, thresh3]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
