#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""YouDao TTS Module"""

__author__ = 'Djl'

import json


class GetMediaFilesNamesRep:
    def __init__(self, result: [], error: object):
        self.result = result
        self.error = error

    @staticmethod
    def decode(code):
        rep_dict = json.loads(code)
        return GetMediaFilesNamesRep(rep_dict.get("result"), rep_dict.get("error"))

    def encode(self):
        return {
            "result": self.result,
            "error": self.error
        }
