#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import logging
from .utils import remove_comments, merge_dict

CURRENT_DIRECTORY = os.getcwd()
DIR = os.path.dirname(os.path.realpath(__file__))

class ManageFile(object):

    def __init__(self, ff, sf):

        self.first_file = self.generate_dict_libs(ff)
        self.second_file = self.generate_dict_libs(sf)

    def open_file(self, file):

        try:
            return open(file, 'r').read()
        except Exception as e:
            logging.error(e)
            raise

    def generate_dict_libs(self, file):

        text = remove_comments(self.open_file(file))

        lib_list = []

        for item in text.split('\n'):

            item = item.split('==')

            if len(item) == 1:
                item.append('')

            lib_list.append(tuple(item))

        return dict(lib_list)

    def show(self):

        print('------------ first_file ------------')
        print(self.first_file)

        print('------------ second_file ------------')
        print(self.second_file)

class Merge(object):

    def __init__(self, mf):

        self.manage_file = mf
        self.dict_libs = {}

        self.merge_dict_libs()

    def merge_dict_libs(self):

        (self.dict_libs, self.error_count) = merge_dict(
            self.manage_file.first_file,
            self.manage_file.second_file
        )

    def generate_requirements_txt(self):

        txt = ''

        for key, value in self.dict_libs.items():
            if len(value):
                txt += ''.join('{}=={}\n'.format(key, value))
            else:
                txt += ''.join('{}\n'.format(key))


        file_path = './requirements-merged.txt'
        count = 0

        while os.path.exists(file_path):

            count += 1
            file_path = './requirements-merged({}).txt'.format(count)

        mode = 'wx' if sys.version_info[0] < 3 else 'x'
        f = open(file_path, mode)
        f.write(txt)
        f.close()

        print('create new file {}'.format(file_path))
        if self.error_count > 0:
            print('WARN: {} values failed to merge.'.format(self.error_count), file=sys.stderr)
            sys.exit(1)
