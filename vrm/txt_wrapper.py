#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vrm.line_wrapper import LineWrapper

class TxtWrapper(object):

    def __init__(self, file_path):
        super().__init__()
        self.txt_path = file_path
        self.lines = []
        self.remove_bom(self.txt_path)

    def remove_bom(self, file_path):
        content = None
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def load_lines(self):
        with open(self.txt_path, 'r', encoding='utf-8') as file:
            for line in file:
                lw = LineWrapper(line)
                self.lines.append(lw)
            print(len(self.lines))

    def list_duplicate_line(self):
        pre_line_word = None
        for lw in self.lines:
            line_word = lw.is_word_in_line(r'(設\s*定)|(解\s*除)|(巡\s*查)')
            
            if line_word != pre_line_word:
                pass
            elif line_word is not None and line_word == pre_line_word:
                lw.print_line()
            pre_line_word = line_word