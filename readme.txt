★今回のアプリは3.11と3,12で使用できることを確認

★以下のように仮想環境を作成してアプリ開発を行う
⇒exe化するうえで特定のモジュール(imp)がpython version(3.11と3,12)に対応していないため

◆仮想環境作成
0.事前準備
0.1.pythonのバージョン確認
  py --version
0.2.Python実行ファイル(python.exe)の場所
  py --list-paths
0.3.インストールしたいpythonパッケージをリスト化したテキストファイルを作成
  pip freeze > requirements.txt

1.python公式から特定のversionをinstall
2.作業フォルダに移動
3.py -3.11 -m venv venv　
4..\venv\Scripts\activate
5.pip install -r requirements.txt

◆pythonスクリプトを実行可能なexeファイルに変換
pyinstaller .\test.py --onefile

◆仮想環境の無効化
deactivate

◆仮想環境の削除
venvファイルごと削除する
