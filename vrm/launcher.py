#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == "__main__":
    with open('./res/inputs/D0035_01.txt', 'r') as file:
        for line in file:
            print(line)
            if re.search('設定', line):
                print(re.search('設定', line).group())
            else:
                print(None)
