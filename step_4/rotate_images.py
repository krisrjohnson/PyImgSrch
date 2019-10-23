import pathlib, imutils, numpy, cv2, argparse
#http://john.freml.in/opencv-rotation

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', default='./pill_img.png', type=str)
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

# imutils has rotate() and rotate_bound(), the latter keeps the entire img
# both are built on cv2 Affine Transformation matrices
for angle in range(0, 360, 15):
    rotated = imutils.rotate(img, angle)
    cv2.imshow('rotated', rotated)
    cv2.waitKey(0)

for angle in range(0, 360, 15):
    rotated = imutils.rotate(img, angle)
    cv2.imshow('rotated w bound', rotated)
    cv2.waitKey(0)