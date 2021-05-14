# -*- coding: utf-8 -*-
import base64

import requests
import time

from anki.model.GetMediaFilesNamesReq import GetMediaFilesNamesReq
from anki.model.Node import Node


def anki_command(url, data):
    return requests.post(url, json=data)


def store_media_file(voice_name: str, voice: []):
    millis = int(round(time.time() * 1000))
    file_name = f"{voice_name}_{millis}.mp3"
    # voice_code = base64.b64encode(voice)
    voice_code = str(base64.b64encode(voice), "utf8")

    return {
        "action": "storeMediaFile",
        "version": 6,
        "params": {
            "filename": file_name,
            "data": voice_code
        }
    }


def get_media_files_names(voice_name: str):
    return GetMediaFilesNamesReq(voice_name).encode()


def generate_add_note_data(add_node: Node):
    return {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "temp",
                "modelName": add_node.model.name,
                "fields": add_node.model_fields,
                "options": {
                    "closeAfterAdding": True
                },
                "tags": add_node.tags
                # ,
                # "audio": [{
                #     "url": "http://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                #     "filename": "yomichan_ねこ_猫.mp3",
                #     "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                #     "fields": [
                #         "发音"
                #     ]
                # }]
            }
        }
    }
