import re
# 正規表現で複数の文字列を検索

MOJI = r"あいうえお \aaa\bbb\ccc\ddd111 かきくけこ"
START = r"\\aaa\\bbb"
END= "ddd111"

print(MOJI) # あいうえお \aaa\bbb\ccc\ddd111 かきくけこ
print("##")
print(re.findall(f'{START}|{END}',MOJI))
print("##")
print("\n")