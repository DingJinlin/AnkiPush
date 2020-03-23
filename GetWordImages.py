import requests
import json

url = "http://dict.youdao.com/search?q=straight&keyfrom=new-fanyi.smartResult"
r = requests.get(url)
print(r.text)
# data2 = json.loads(r.text)
# print ("image: ", data2['img'])
