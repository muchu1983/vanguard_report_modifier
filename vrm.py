#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from vrm.txt_wrapper import TxtWrapper

def open_txt_file():
    root = tk.Tk()
    root.withdraw()
    txt_path = filedialog.askopenfilename(
        title="選擇txt檔案",
        filetypes=[("文本文件", "*.txt")])
    print(txt_path)
    txt_w = TxtWrapper(txt_path)
    txt_w.load_lines()
    txt_w.list_duplicate_line()

if __name__ == "__main__":
    #open_txt_file()
    
    while True:
        print("請輸入指令：'open'選檔，'exit'结束：")
        line = input()
        if line == 'exit':
            break
        elif line == 'open':
            open_txt_file()
    
