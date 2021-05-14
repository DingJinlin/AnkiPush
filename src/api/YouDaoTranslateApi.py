# -*- coding: utf-8 -*-

import uuid
import requests
import hashlib
import time

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '1170ab7ad32e37fa'
APP_SECRET = 'ADvrYcEg0I0vQUHkca7wldFQnFcu5HFv'


def encrypt(sign_str):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(sign_str.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(word):
    q = word

    data = {
        'from': 'en',
        'to': 'zh-CHS',
        'signType': 'v3'}
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    sign_str = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(sign_str)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    # data['vocabId'] = "您的用户词表ID"

    response = do_request(data)
    content_type = response.headers['Content-Type']
    if content_type == "audio/mp3":
        millis = int(round(time.time() * 1000))
        file_path = "./" + str(millis) + ".mp3"
        fo = open(file_path, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        print(response.content)


if __name__ == '__main__':
    connect('snake')
