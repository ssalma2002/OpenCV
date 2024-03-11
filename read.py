import cv2 as cv

#read images 
# '''
# img = cv.imread("pics/cat3.jpg")
# cv.imshow("Cat",img)
# cv.waitKey(0)
# '''
#reading videos

capture = cv.VideoCapture("videos/cute_dog.mp4")

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(100) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()