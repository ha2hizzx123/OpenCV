#OpenCV모듈 불러오기
import cv2 as cv
#imread : 이미지 파일일 읽어들여 메모리에 저장함 첫 부분에 읽을 파일을 적고 두번째 아규먼트는 파일을 읽을 방식을 말한다.
#cv2.IMREAD_COLOR : 기본값으로 컬러 이미지로 읽어들임
#cv2.IMREAD_GRAYSCALE : 그레이스케일 이미지로 읽어들임
#cv2.IMREAD_UNCHANGED : 알파 채널을 포함한 이미지를 그대로 읽어들임
img_color = cv.imread('images.jpg', cv.IMREAD_COLOR)
#윈도우에 이미지가 보이도록 함
cv.namedWindow('Show Image')

#이미지창 띄우기
cv.imshow('Show Image', img_color)

#키 입력이 일을때까지 해당밀리초 기다림 0일시 무한정 기다림
#시간이 다 되었거나 키가 입력되었을때 종료됨
cv.waitKey(0)

#키 입력이 되었을때 이미지가 IMREAD_GRAYSCALE로 바뀜
img_gray = cv.imread('images.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Show Image', img_gray)
cv.waitKey(0)
img_unchanged = cv.imread('images.jpg', cv.IMREAD_UNCHANGED)
#세로운 창을 별도로 만든다.
cv.imshow('Show Image 2', img_unchanged)
cv.waitKey(0)

#이미지 파일을 만든다.
cv.imwrite('images2.jpg',img_gray)
cv.destroyAllWindows()#열린 모든 창을 닫음