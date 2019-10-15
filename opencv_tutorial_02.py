import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
# ap.add_argument("-i", "--image", required=False, default='./tetris_blocks.png')
args = vars(ap.parse_args())

def cv2img(img):
	cv2.imshow('name', img)
	cv2.waitKey(0)

img = cv2.imread(args["image"])
cv2img(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
edged = cv2.Canny(gray, 30, 150)

cv2img(edged)

thresh_copy = thresh.copy()
cv2.putText(thresh_copy, 'Thresh!', (10,25), \
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2) #thresh is a single channel

cv2img(thresh_copy)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = img.copy()

for c in cnts:
	cv2.drawContours(output, [c], -1, (240,0,159), 3)
	# cv2.imshow("contours", output)
	# cv2.waitKey(0)

text = f"I found {len(cnts)} objects"
cv2.putText(output, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
cv2img(output)

#Erosions dilations
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2img(mask)

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2img(mask)

#combine first and second img
mask = thresh.copy()
output = cv2.bitwise_and(img, img, mask=mask)
cv2img(output)