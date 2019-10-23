# REPO for going through [PyImageSearch](https://pyimagesearch.com) tutorials.

[Start](https://www.pyimagesearch.com/start-here/) point

First ["week"](https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/)

Using miniconda to manage environments: `conda --create PyImgSrch --file conda-spec-file.txt`
Specfile created by
```bash
conda create --name PyImgSrch py=3.7
conda activate PyImgSrch
#conda installs and pip installs;
conda list --explicit > conda-spec-file.txt
```

----
Some useful pseudo-code

downloading an img url off the web
```python
import requests

path = 'some/path/filename_to_save_as.png'
url = 'https://some_Url.com/img.png'
#could use pathlib parts method to strip out the imgname from the url
#or even a split on '/'
try:
  r = requests.get(url, timeout=10)
  f = open(path, 'wb')
  f.write(r.content)
  f.close()
  print(f'saved file to {path}')
except:
  print('error saving file')
```

Handling displaying images from running python on terminal:
```python
img = cv2.cvtColor(cv2.imread('somepath'), cv2.COLOR_BGR2RGB) #since we'll be displaying

while True:
  cv2.imshow('img', img)
  key = cv2.waitKey(1) & 0xFF
  if key==ord('q'): break
```
