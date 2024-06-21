import openpyxl
import pandas as pd

# シート全体を検索
def search_entire_sheet(ws, keyword):
    result = {}
    for col in ws.columns:
        for cell in col:
            # セルのデータを文字列に変換
            try:
                value = str(cell.value)
            except:
                continue
            # キーワードに一致するセルの番地を取得
            for key in keyword:
                if value == key:
                    result[key] = []
                    # キーワードの列のアルファベット
                    result[key].append(openpyxl.utils.get_column_letter(cell.column))
                    # キーワードの行の数値
                    result[key].append(str(cell.row))
    return result

if __name__ == '__main__':
    filename = 'test.xlsx'
    wb = openpyxl.load_workbook(filename)
    ws = wb['Sheet1']
    keywords = ["やること","時間帯"]

    # 関数の実行：シート全体を検索
    result = search_entire_sheet(ws, keywords)
    print(result)

