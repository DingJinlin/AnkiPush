#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""YouDao TTS Module"""

__author__ = 'Djl'

import json


class GetMediaFilesNamesReq:
    def __init__(self, voice_name: str):
        self.voice_name = voice_name

    @staticmethod
    def decode(code):
        rep_dict = json.loads(code)
        return GetMediaFilesNamesReq(rep_dict.get("params").get("pattern"))

    def encode(self):
        return {
            "action": "retrieveMediaFile",
            "version": 6,
            "params": {
                "pattern": f"{self.voice_name}_*.txt"
            }
        }
