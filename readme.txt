★以下のように仮想環境を作成してアプリ開発を行う
⇒exe化するうえで特定のモジュール(imp)が最新のpython versionに対応していないため

◆仮想環境作成
1.python公式から特定のversionをinstall
2.作業フォルダに移動
3.py -3.11 -m venv venv
4.pip freeze > requirements.txt
5.venv\Scripts\activate
6.pip install -r requirements.txt

◆pythonスクリプトを実行可能なexeファイルに変換
pyinstaller .\test.py --onefile

◆仮想環境の無効化
deactivate

◆仮想環境の削除
venvファイルごと削除する
