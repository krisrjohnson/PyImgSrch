import argparse
import requests
import pathlib

ap = argparse.ArgumentParser()
ap.add_argument('-u', '--url', required=True, help='url of img to download')
ap.add_argument('-f','--fn', required=True, type=str, help='output file name')
ap.add_argument('-d', '--dest', default='assets/images/', type=str, help='output file destination (folder)')
args = vars(ap.parse_args())

try:
    r = requests.get(args['url'], timeout=10)
    f = open(str(pathlib.Path.cwd()/args['dest']/args['fn']), 'wb')
    f.write(r.content)
    f.close()
    print(f'file written to {args["dest"]}{args["fn"]}')
except:
    print('error downloading file')