# import os
# import glob
import pathlib


# # 1)指定したフォルダのフォルダ名を全て取得
# folder_path = "../"
# list = os.listdir(folder_path)
# print(list)

# # 1)をテキストファイルで出力
# output_path = './output.txt'
# with open(output_path,"w") as file:
#     file.write('\n'.join(list))



# # 2)フォルダの中にあるファイル名を全て取得
# file_list = glob.glob("../**/*.*",recursive=True)
# name_list = [os.path.basename(file) for file in file_list]

# # 2)テキストファイルで出力
# output_path = './output.txt'
# with open(output_path,"w") as file:
#     file.write('\n'.join(file_list))


#プログラム2｜mainプロシージャ
def main():
    # Folderpath = os.getcwd()#対象フォルダを指定
    Folderpath = "../"
    outputpath = 'list.txt'#テキストファイルを作成
    f = open(outputpath, mode='w')#テキストファイルを書き込みモードで開く

    GetFolderFileNames(Folderpath, 0, f)#GetFolderFileNames(プログラム3)を呼び出す

#プログラム3｜階層ごとのフォルダやファイルを書き出す関数
def GetFolderFileNames(path, kaiso, f):
    files = pathlib.Path(path).glob('*')#その階層のフォルダやファイルを取得

    # プログラム4｜フォルダやファイルを一つずつ書き出す
    for file in files:
        output = '\t' * kaiso + file.name + '\n'
        f.write(output)

        # プログラム5｜フォルダの場合、その下の階層のフォルダやファイルをGetFolderFileNames(プログラム6)を呼び出す
        if file.is_file() == False:
            GetFolderFileNames(file, kaiso+1, f)

#プログラム6｜mainを呼び出す
if __name__ == "__main__":
    main()


