#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""Word model"""

__author__ = 'Djl'

import csv
from model.Word import Word

CSV_SUFFIX = ".csv"


def read_words(file_path: str):
    if file_path.endswith(CSV_SUFFIX):
        words = []
        csv_file = open(file_path, "r")
        reader = csv.reader(csv_file)
        for item in reader:
            # 忽略第一行
            if reader.line_num == 1:
                continue
            words.append(Word(item[0], item[1]))
        csv_file.close()
        return words
    else:
        raise ValueError("file isn't csv file.")


