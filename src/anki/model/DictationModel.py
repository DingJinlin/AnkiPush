#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""YouDao TTS Module"""

__author__ = 'Djl'

from anki.model.Model import Model


class DictationModel(Model):
    def __init__(self):
        super().__init__('无图单词 填写', ("单词", "中文", "发音"))
