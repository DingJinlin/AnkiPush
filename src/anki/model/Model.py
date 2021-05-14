#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""YouDao TTS Module"""

__author__ = 'Djl'

# from loguru import logger

'''
"note": {
    "deckName": "temp",
    "modelName": "无图单词 填写",
    "fields": {
        "单词": eng,
        "中文": cn,
        "发音": voice
    },
    "options": {
        "closeAfterAdding": True
    },
    "tags": [
        ""
    ]
}
'''


class Model:
    def __init__(self, name: str, fields: []):
        self.name = name
        self.fields = fields

    def to_str(self):
        return {
            'name': self.name,
            'fields': self.fields
        }
