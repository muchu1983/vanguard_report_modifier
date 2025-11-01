#!/usr/bin/env python
# -*- coding: utf-8 -*-
from invoke import task
import shutil

@task
def build_win(ctx):
    #打包exe
    ctx.run("pyinstaller --onefile vrm.py")
    #複製exe到根目錄下
    exe_source_file = "./dist/vrm.exe"
    exe_target_file = "./vrm.exe"
    shutil.copy2(exe_source_file, exe_target_file)
    #刪除打包產生的build及dist資料夾
    build_folder_path = "./build"
    shutil.rmtree(build_folder_path)
    dist_folder_path = "./dist"
    shutil.rmtree(dist_folder_path)
    
    print("build_exe successfully!")

@task
def build_linux(ctx):
    #打包exe
    ctx.run("pyinstaller --onefile vrm.py")
    #複製exe到根目錄下
    bin_source_file = "./dist/vrm"
    bin_target_file = "./vrm"
    shutil.copy2(bin_source_file, bin_target_file)
    #刪除打包產生的build及dist資料夾
    build_folder_path = "./build"
    shutil.rmtree(build_folder_path)
    dist_folder_path = "./dist"
    shutil.rmtree(dist_folder_path)
    
    print("build_exe successfully!")