:pythonファイルを同じディレクトリに置いてダブルクリック
@echo off
cd /d %~dp0
py file.py
pause