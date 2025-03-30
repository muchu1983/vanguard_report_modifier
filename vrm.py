#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from vrm.txt_wrapper import TxtWrapper

def open_txt_file():
    txt_path = filedialog.askopenfilename(
        title="選擇.txt檔案",
        filetypes=[("文本文件", "*.txt")])
    print(txt_path)
    txt_w = TxtWrapper(txt_path)
    txt_w.list_duplicate_set_and_unset()
    txt_w.list_duplicate_patrol()

def show_ui():
    root = tk.Tk()
    root.title("先鋒報表")
    button = tk.Button(
        root,
        text="選擇.txt檔案",
        command=open_txt_file,
        width=40,
        height=3
    )
    button.pack(pady=5)  # 将按钮添加到窗口
    root.mainloop()

if __name__ == "__main__":
    # develop 區
    open_txt_file()
    
    # invoke build-exe 區
    # while True:
    #     print("請輸入指令：'open'選檔，'button'圖形介面, 'exit'结束：")
    #     line = input()
    #     if line == 'exit':
    #         break
    #     elif line == 'open':
    #         open_txt_file()
    #     elif line == 'button':
    #         show_ui()
