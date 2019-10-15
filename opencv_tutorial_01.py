import imutils
import cv2

img = cv2.imread('jp.jpg')
h,w,d = img.shape
roi = img[60:160, 200:260]
resized = cv2.resize(img, (200,200)) #cv2.INTER_AREA

# cv2.imshow('roi', roi)
# cv2.imshow('img', img)

# resized = cv2.resize(img, (300, int(300. 300. * h/w )))
resized = imutils.resize(img, width=300)

cv2.imshow('resized', resized)

# rotate image
center = (w//2, h//2)
# M = cv2.getRotationMatrix2D(center, -45, 1.0); rotated = cv2.warpAffine(img, M, (w,h))
# rotated = imutils.rotate(img, -45)
# rotated = imutils.1(img, 45)
# blurred = cv2.GaussianBlur(img, (11,11), 0) #11x11 kernel
# output = img.copy()
# cv2.rectangle(output, (200,60), (260,160), (0,0,255), 2) #inplace 2px box
# cv2.circle(output, (230,110), 20, (0,255,0), -1) #-1 means filled
# cv2.line(output, (60,20), (400,200), (255,0,0), 5)
output = img.copy()
cv2.putText(output, 'Jurassic Park!', (10,25), \
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)


cv2.imshow('rectangle', output)

cv2.waitKey(0)

