#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from vrm.line_wrapper import LineWrapper

class TxtWrapper(object):

    def __init__(self, txt_path):
        super().__init__()
        self.txt_path = txt_path
        self.lines = []
        self.remove_bom()
        self.load_lines()
        self.remove_word_in_line(r',\d{0,5},$') #刪除尾部數字
        self.remove_word_in_line(r'未知原因')

    def remove_bom(self):
        content = None
        with open(self.txt_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        with open(self.txt_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def load_lines(self):
        with open(self.txt_path, 'r', encoding='utf-8') as file:
            for line in file:
                lw = LineWrapper(line)
                self.lines.append(lw)
            print('讀取總筆數：{}'.format(len(self.lines)))

    def list_duplicate_set_and_unset(self):
        pre_line_word = None
        for lw in self.lines:
            line_time = lw.is_word_in_line(r'(^\d\d/\d\d[\s,]\d\d:\d\d)')
            line_word = lw.is_word_in_line(r'(設\s*定)|(巡\s*設)|(解\s*除)')
            if line_word is not None:
                line_word = re.sub(r'\s+', '', line_word)  #清除空白
                if line_word =='巡設':
                    line_word = '設定'  #巡設等同設定
                    print('注意：{} 檢查到巡設'.format(line_time))
                if line_word == pre_line_word:
                    print('重覆：{} 內容：{}'.format(line_time, lw.get_line()))
                pre_line_word = line_word
    
    def remove_word_in_line(self, raw_string):
        pattern = re.compile(raw_string)
        for lw in self.lines:
            new_line = pattern.sub('', lw.get_line())
            lw.set_line(new_line)
        self.save_txt()

    def save_txt(self):
        with open(self.txt_path, 'w', encoding='utf-8') as file:
            file.writelines(lw.get_line() for lw in self.lines)

    def list_duplicate_patrol(self):
        pattern_patrol_word = re.compile(r'(巡\s*查)')
        pattern_patrol_day = re.compile(r'^\d\d/\d\d')
        patrol_count = 0
        patrol_day_record = []
        for lw in self.lines:
            patrol_word = pattern_patrol_word.search(lw.get_line())
            patrol_day = pattern_patrol_day.search(lw.get_line())
            if patrol_word is not None and patrol_day is not None:
                if patrol_day.group() in patrol_day_record:
                    print('重覆巡查日：{}'.format(lw.get_line()))
                patrol_count += 1
                patrol_day_record.append(patrol_day.group())
        print('總巡查筆數：{}'.format(patrol_count))