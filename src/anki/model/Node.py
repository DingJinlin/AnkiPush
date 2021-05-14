#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""YouDao TTS Module"""

__author__ = 'Djl'

import json
from loguru import logger

from anki.model.DictationModel import DictationModel
from anki.model.Model import Model

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


class Node:
    def __init__(self, dock_name, model: Model, fields: [], tags: [] = []):
        self.dock_name = dock_name
        self.model = model
        self.tags = tags
        self.model_fields = dict(zip(model.fields, fields))

    def to_str(self):
        return {
            'deck_name': self.dock_name,
            'model': self.model.to_str(),
            'model_fields': self.model_fields,
            'tags': self.tags
        }


if __name__ == '__main__':
    model_obj = DictationModel()
    node = Node("temp", model_obj, ("snake", "蛇", "file:\\\\snake.mp3"))
    logger.debug(json.dumps(node.to_str(), ensure_ascii=False, indent=2))
