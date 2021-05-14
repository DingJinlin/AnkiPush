#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""Word model"""

__author__ = 'Djl'

import json

from loguru import logger

from anki.model.DictationModel import DictationModel
from anki.model.GetMediaFilesNamesRep import GetMediaFilesNamesRep
from anki.model.Node import Node
from api import YouDaoTTSApi, AnkiConnectApi
from util import WordReader, FileUtil

RESOURCES_PATH = "../resources"
ABS_PATH = f"{FileUtil.get_cur_prj_path()}/{RESOURCES_PATH}"
VOICE_FILE_PATH = f"{ABS_PATH}/voices"
WORDS_FILE_PATH = f"{ABS_PATH}/4.1M5-10.csv"
ANKI_URL = "http://10.217.6.46:8765"
ANKI_DOCK_NAME = "word4.1"

if __name__ == '__main__':

    # 获取单词列表
    words = WordReader.read_words(WORDS_FILE_PATH)
    # words = WordReader.read_words("/mnt/linuxDisk/documents/个人/english/4.1M5-10.csv")

    for word in words:
        # 获取现有音频文件名
        repCode = AnkiConnectApi.anki_command(ANKI_URL, AnkiConnectApi.get_media_files_names(word.eng))
        get_media_rep = GetMediaFilesNamesRep.decode(repCode.content)

        voice_file_name = None
        if get_media_rep.result is None:
            # 预读取音频文件
            try:
                voice = FileUtil.read_file(f"{VOICE_FILE_PATH}/{word.eng}.mp3")
            except FileNotFoundError:
                voice = None

            if voice is None:
                # 获取音频文件
                voice_result = YouDaoTTSApi.get_voice(word.eng, 6, VOICE_FILE_PATH)
                if voice_result.content_type == 'file':
                    voice = voice_result.content

            if voice is not None:
                # 上传音频Anki voice
                httpRep = AnkiConnectApi.anki_command(ANKI_URL, AnkiConnectApi.store_media_file(word.eng, voice))
                store_media_rep = GetMediaFilesNamesRep.decode(httpRep.content)
                voice_file_name = store_media_rep.result
        else:
            voice_file_name = get_media_rep.result[0]

        # 检查音频是否存在
        if voice_file_name is not None:
            dictation_model = DictationModel()

            # 上传Anki node
            node = Node(ANKI_DOCK_NAME, dictation_model, (word.eng, word.cn, f"[sound:{voice_file_name}]"))
            logger.debug(json.dumps(node.to_str(), ensure_ascii=False, indent=2))
            node_data = AnkiConnectApi.generate_add_note_data(node)
            AnkiConnectApi.anki_command(ANKI_URL, node_data)
        else:
            logger.error("Not found voice file")
