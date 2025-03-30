#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from typing import Union

class LineWrapper(object):
    
    def __init__(self, line):
        super().__init__()
        self.line = line

    def is_word_in_line(self, word):
        pattern = word
        if re.search(pattern, self.line):
            return re.search(pattern, self.line).group()
        else:
            return None

    def get_line(self) -> Union[None, str]:
        return self.line

    def set_line(self, line):
        self.line = line
