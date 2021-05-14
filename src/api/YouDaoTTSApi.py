#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""YouDao TTS Module"""

__author__ = 'Djl'

import os
import uuid
import requests
import hashlib
from loguru import logger

from api.model.VoiceDataResult import VoiceDataResult
from util import FileUtil

YOUDAO_URL = 'https://openapi.youdao.com/ttsapi'
APP_KEY = '0f998c4d5e37c3cd'
APP_SECRET = 'ZYwZa41uAgSIaj5UIrcBM3p9cnqwUYAE'

RESOURCES_PATH = "../resources"
abs_path = f"{FileUtil.get_cur_prj_path()}/{RESOURCES_PATH}"


def encrypt(sign_str):
    hash_algorithm = hashlib.md5()
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


def get_voice(word, voice_type, file_path=None):
    q = word
    salt = str(uuid.uuid1())
    sign_str = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(sign_str)

    # data = {'langType': 'en-USA', 'appKey': APP_KEY, 'q': q, 'salt': salt, 'sign': sign, 'voice': voice_type}
    data = {
        'langType': 'en',
        'appKey': APP_KEY,
        'q': q,
        'salt': salt,
        'sign': sign,
        'voice': voice_type
    }

    response = do_request(data)
    rep_content_type = response.headers['Content-Type']
    if rep_content_type == "audio/mp3":
        content_type = "file"
        content = response.content

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        FileUtil.write_file(f"{file_path}/{word}.mp3", content)
    else:
        logger.debug(response.content)
        content_type = 'url'
        content = str(response.content, "utf8")

    return VoiceDataResult(content_type, content)


if __name__ == '__main__':
    pass
    result = get_voice("be able to", 6, f"{abs_path}/voices")

    if result.content_type == 'file':
        voice = result.content
    else:
        url = result.content
