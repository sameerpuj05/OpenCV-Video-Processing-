import cv2 as cv
import numpy as np

#Frame rescale function
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#IMAGES

img= img_read = cv.imread('things.jpg')
img = cv.resize(img_read, (720,480), interpolation=cv.INTER_AREA)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('blank',blank)

#dimensions
dimensions = (img.shape[1],img.shape[0])
# crop = img[50:200,200:400]
# cv.rectangle(img,(0,0),(320,320),(255,0,0),thickness=5)
# cv.rectangle(img,(img.shape[1]//4,img.shape[0]//4),(img.shape[1]//8,img.shape[0]//8),(0,0,255),thickness=cv.FILLED)

#color
# img[100:250,200:400]=0,255,0 #Change a part of image colour
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #RGB to GRAY
# b,g,r=cv.split(img)
# merged=cv.merge([b,g,blank])

#transform
# cv.imshow("trans", translate(img,100,100))
# cv.imshow("rotate", cv.warpAffine(img, cv.getRotationMatrix2D((320,320),90,1.0),dimensions))
# cv.imshow("flip",cv.flip(img,1))


#edit
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)     #blur

# ret, thresh = cv.threshold(gray, 199, 255, cv.THRESH_BINARY)
# cv.imshow('thres',ret)

# canny = cv.Canny(gray,125,175) #EDGE cascade
# contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours found !')
# print((heirarchies.shape))
# cv.drawContours(blank, contours, -1, (255,255,255), 1)
# cv.imshow('bl', img)
# cv.imshow('cn',canny)

#bitwise
# rect= cv.rectangle(blank.copy(),(img.shape[1]//4,img.shape[0]//4),((img.shape[1]//2+img.shape[1]//4),(img.shape[0]//2+img.shape[0]//4)),(255,0,0),thickness=-1)
cir= cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),img.shape[1]//4,255,-1)
# bitwise_and=cv.bitwise_and(rect,cir)
# bitwise_or=cv.bitwise_or(rect,cir)
# bitwise_not=cv.bitwise_not(rect)

cv.imshow('rect',img)
cv.imshow('cir',cir)
bitwise_and=cv.bitwise_and(img,img,mask=cir) #not very clear
cv.imshow('not',bitwise_and)



key=cv.waitKey(0)
if key == 'd':
    cv.destroyAllWindows()

#VIDEOS

# video = cv.VideoCapture(0)
# video.set(3,640)
# video.set(4,640)
# while True:
#     isTrue, frame = video.read()
#     cv.imshow('video',frame)

#     rescaledFrame = rescaleFrame(frame, scale=0.2)
#     cv.imshow('video_rescaled',rescaledFrame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# video.release()
# cv.destroyAllWindows()

# # -215 assertion failed -> indicates frame cannot be read by opencv at specified location
