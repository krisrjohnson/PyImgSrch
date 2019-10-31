
################################################
'''
Have a list of URLs downloaded using code from 
https://msollami.com/code/2017/1/3/google-image-scraper

Download valid urls
test cv2 can open downloaded images
flip through photos allowing user to delete undesirables ('d' key)
output a list of final "clean" urls, both valid and desirable

TODO: add 'n' key press to go to previous photo
TODO: abstract/refactor the open image path and delete section
TODO: flag to enable/disable manual flipping through all the downloaded images
'''
################################################
# CLI args and some setup
import argparse, requests, cv2, os, pathlib, glob

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", default='./assets/images/charcoal_drawings/charcoal_urls.txt', type=str)
ap.add_argument('-o', "--output", default='./assets/images/charcoal_drawings', type=str)
args = vars(ap.parse_args())

rows = open(args["urls"]).read().strip().split("\n")

urls_dict = {}
for idx, url in enumerate(rows):
    urls_dict[idx] = url

    
################################################
#loop over urls and write valid urls to disk - creating a dict of urls to img idx
idx_to_pop = []
for idx, url in urls_dict.items():
    try:
        r = requests.get(url, timeout=3)
        p = pathlib.Path(args['output'])/f'{str(idx).zfill(8)}.png'
        f = open(str(p), "wb")
        f.write(r.content)
        f.close()
        print(f'[INFO]: downloaded {p}')
    except:
        print(f'[INFO]: error dowonloading {p} ... skipping')
        idx_to_pop.append(idx)

_ = [urls_dict.pop(idx) for idx in idx_to_pop]


################################################
# loop over files written to disk and delete invalids - cv2 can't load or I don't want
idx_to_pop = []

for idx in urls_dict.keys():
    continue_delete_loop = True
    delete = False
    image_path = str(pathlib.Path(args['output'])/f'{str(idx).zfill(8)}.png')

    try:
        image = cv2.imread(image_path)
        if image is None:
            delete = True
        else: 
            while continue_delete_loop:
                cv2.imshow('img', image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('d'):
                    delete = True
                    continue_delete_loop = False
                if key == ord('q'):
                    continue_delete_loop = False
    except:
        print('Except')
        delete = True
        
    cv2.destroyAllWindows()

    if delete:
        print(f'[INFO]: deleting {image_path}')
        os.remove(image_path)
        idx_to_pop.append(idx)

_ = [urls_dict.pop(idx) for idx in idx_to_pop]

final_urls = pathlib.Path(args['output'])/f'final_{pathlib.Path(args["urls"]).parts[-1]}'
f = open(str(final_urls), "w")
for url in urls_dict.values():
    f.write(url+'\n')
f.close()
