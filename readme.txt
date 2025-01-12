★今回のアプリは3.11と3,12で使用できることを確認

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
⇒今回はexeファイル化しない
pyinstaller .\test.py --onefile

◆仮想環境の無効化
deactivate

◆仮想環境の削除
venvファイルごと削除する

◆git管理
リポジトリを新規作成する
git init
ディレクトリの現在の状態を確認する
git status
ワークツリーからインデックスにコミットしたいファイルを登録する
git add ファイル名
インデックス上のファイルを更新する
git commit -m "コメント"
ログを出力する
git log
新規ブランチを作成して切り替える
git checkout -b "新規ブランチ名"
対象ブランチに切り替える
git checkout "移動先ブランチ名"
対象のコミットを元に戻す
git revert <コミットID>