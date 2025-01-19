#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

class LineWrapper(object):
    """docstring for LineWrapper"""
    def __init__(self, line):
        super(LineWrapper, self).__init__()
        self.line = line

    def is_word_in_line(self, word):
        pattern = word
        print(self.line)
        if re.search(pattern, self.line):
            print(re.search(pattern, self.line).group())
        else:
            print(None)
