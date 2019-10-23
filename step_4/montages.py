from imutils import build_montages
import argparse, random, cv2
import pathlib
import os
import glob


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', default='../assets/images/', help='path to input dir of imgs')
ap.add_argument('-s', '--sample', type=int, default=21)
args = vars(ap.parse_args())

base_path = pathlib.Path.cwd()/args['images']
print(f'path looking at: {base_path}')

imagePaths = []
for fn in os.listdir(str(base_path)):
    if pathlib.Path(fn).parts[-1][-4:] == '.png':
        imagePaths.append(str(base_path/fn))

random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]] #python can handle this being > len(imagePaths)


images = []
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)
    print(f'appending: {pathlib.Path(imagePath).parts[-1]}')

if len(images) > 0:
    montages = build_montages(images, (128,196), (7,3)) #img_list, size to reshape, colsxrows

    for montage in montages:
        cv2.imshow('montage', montage)
        cv2.waitKey(0)
else:
    print('images loaded improperly or no images in input path')