#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

class LineWrapper(object):
    """docstring for LineWrapper"""
    def __init__(self, line):
        super().__init__()
        self.line = line

    def is_word_in_line(self, word):
        pattern = word
        if re.search(pattern, self.line):
            return re.search(pattern, self.line).group()
        else:
            return None

    def print_line(self):
        print(self.line)
