#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""Word model"""

__author__ = 'Djl'

import os


def find_voice_file(voice_files_path, voice_name):
    file_names = os.listdir(voice_files_path)

    for file_name in file_names:
        if file_name.startswith(voice_name):
            return f"{file_name}/{voice_files_path}"

    return None


def save_voice_file(voice_files_path, voice_name, voice):
    if voice_files_path is not None:
        file = voice_files_path + voice_name + ".mp3"
    else:
        raise FileNotFoundError

    fo = open(file, 'wb')
    fo.write(voice)
    fo.close()
    return file
