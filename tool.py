import csv

# CSVファイルの読み込み
list = []
with open('sample.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        list.append(row)

print(list)

# \を挿入


