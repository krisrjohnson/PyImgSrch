# pip install requests
from imutils import paths
import argparse, requests, cv2, os, pathlib, glob

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", default='C:/Users/Kris Johnson/Downloads/charcoal_urls.txt.txt', type=str)
ap.add_argument('-o', "--output", default='C:/Users/Kris Johnson/Desktop/gitrepos/PyImgSrch/charcoal_imgs', type=str)
args = vars(ap.parse_args())

rows = open(args["urls"]).read().strip().split("\n")
total = 0

################################################
#loop over urls and write valid urls to disk
for url in rows:
    try:
        r = requests.get(url, timeout=10)
        p = pathlib.Path(args['output'])/f'{str(total).zfill(8)}.png'
        f = open(str(p), "wb")
        f.write(r.content)
        f.close()
        print(f'[INFO]: downloaded {p}')
        total += 1
    except:
        print(f'[INFO]: error dowonloading {p} ... skipping')

################################################
# loop over files written to disk and delete invalids
for imagePath in paths.list_images(args['output']):
    delete = False
    continue_delete_loop = True

    try:
        image = cv2.imread(imagePath)
        if image is None:
            delete=True
        else:
            while continue_delete_loop:
                cv2.imshow('img', image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('d'):
                    delete=True
                elif key == ord('esc'):
                    continue_delete_loop = False
                elif key == ord('q'):
                    break #need keypress to break
    except:
        print("Except")
        delete = True
    cv2.destroyAllWindows() #prolly not necessary

    if delete:
        print(f'[INFO]: deleting {imagePath}')
        os.remove(imagePath)
