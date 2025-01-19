#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from vrm.line_wrapper import LineWrapper

if __name__ == "__main__":
    with open('./res/inputs/D0233.txt', 'r') as file:
        for line in file:
            lw = LineWrapper(line)
            lw.is_word_in_line('(設定)|(解除)|(巡查)')