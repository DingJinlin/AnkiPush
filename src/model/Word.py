#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""Word model"""

__author__ = 'Djl'


class Word:
    def __init__(self, eng: str, cn: str):
        self.eng = eng
        self.cn = cn

    def to_str(self):
        return {
            'eng': self.eng,
            'cn': self.cn
        }
