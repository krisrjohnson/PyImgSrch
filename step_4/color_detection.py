import numpy as np
import argparse, cv2, pathlib

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', default='../assets/images/colorful_img.png', type=str)
args = vars(ap.parse_args())

img = cv2.imread(str(pathlib.Path.cwd()/args['image']))

# cv2.imshow('image', img)
# cv2.waitKey(0)

    
color_boundaries = [
    ([0, 0, 200], [100, 100, 255]), #red #lower->upper boundaries for BGR colors
    ([200,0,0], [255,100,100]), #blue
    ([0,150,150], [100,255,255]), #orange
    ([103,86,65], [145,133,128]) #gray
]

for (lower, upper) in color_boundaries:
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')
    
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('image', np.hstack([img, output]))
    cv2.waitKey(0)
