import os
import pathlib

folder_path = r"C:\Users\teradatakayuki\Desktop\job"

# 1)指定したディレクトリ内のファイルパスを全て表示する
def show_file_path():
    for current_dir, sub_dirs, files_list in os.walk(folder_path): 
        for file_name in files_list:
            print(os.path.join(current_dir,file_name))

# 2)指定したディレクトリ内のサブフォルダ名パスを全て表示する
def show_subfolder_path():
    for current_dir, sub_dirs, files_list in os.walk(folder_path): 
        for sub_dir_name in sub_dirs:
            print(os.path.join(current_dir,sub_dir_name))

# 3)指定したディレクトリ内のサブフォルダ名を全て取得する
def get_subfolder_name():
    for current_dir, sub_dirs, files_list in os.walk(folder_path):
            print(u"現在のディレクトリは {} です".format(current_dir)) 
            print(u"サブディレクトリは {} です".format(sub_dirs)) 


if __name__ == '__main__':
    # show_subfolder_path()
    get_subfolder_name()











''' 投稿一つ目
# 検索したい文字列
MOJI = "AAA-BBB-CCC"
# 検索したい文字
JUDGE = "C"

l = []
CERT = None

if JUDGE in MOJI:
    # 検索したい文字がある時
    print(f"{JUDGE} is in {MOJI}")
    # 特定の位置で文字列を区切る
    l = MOJI.split("-")
    for i in l:
        if JUDGE in i:
            # 検索文字が含まれる文字列の格納
            CERT =  i
            print(CERT)

else:
    # 検索したい文字がない時
    print(f"{JUDGE} is not in {MOJI}")
'''
