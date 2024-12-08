import tkinter as tk
from tkinter import scrolledtext, Spinbox, StringVar, OptionMenu
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import webbrowser
import json

# JSONファイルから検索キーワードを読み込む
def load_keywords_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data.get('keywords', {})

# 翻訳を実行
def translate_text(text):
    translated = translator.translate(text, src='ja', dest='en')
    return translated.text

def search_google_scholar(query, num_pages, start_year, end_year):
    base_url = 'https://scholar.google.com/scholar'
    params = {
        'q': query,
        'hl': 'en',
        'as_ylo': start_year,
        'as_yhi': end_year
    }
    results = []

    for page in range(num_pages):
        params['start'] = page * 10
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        for result in soup.find_all('div', class_='gs_ri'):
            title = result.find('h3', class_='gs_rt').text
            link = result.find('a')['href']
            translated_title = translate_text(title)
            details = result.find('div', class_='gs_a').text
            authors, rest = details.split(' - ', 1)
            authors_list = authors.split(',')[:3]  # 最初の3人の著者を取得
            citation = result.find('div', class_='gs_fl').find_all('a')[2].text
            results.append((title, translated_title, link, citation, authors_list))
    
    return results

def on_search():
    keyword_jp = keyword_spinbox.get()
    query = translate_text(keyword_jp)
    num_pages = int(pages_spinbox.get())
    start_year = int(start_year_spinbox.get())
    end_year = int(end_year_spinbox.get())
    results = search_google_scholar(query, num_pages, start_year, end_year)
    
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    
    for original_title, translated_title, link, citation, authors in results:
        authors_str = ", ".join(authors)
        text_area.insert(tk.END, f'Original: {original_title}\nTranslation: {translated_title}\nCitations: {citation}\nAuthors: {authors_str}\n')
        
        # ハイパーリンクを追加
        text_area.insert(tk.END, "Link", link)
        text_area.insert(tk.END, f': {link}\n\n')
        text_area.insert(tk.END, '-'*80 + '\n')  # 線引き追加
        text_area.tag_config(link, foreground="blue", underline=True)
        text_area.tag_bind(link, "<Button-1>", lambda e, url=link: webbrowser.open_new(url))
    
    text_area.config(state=tk.DISABLED)

def update_keywords(*args):
    genre = genre_var.get()
    keywords = keywords_by_genre.get(genre, [])
    keyword_var.set(keywords[0] if keywords else "")
    keyword_spinbox["values"] = keywords

def open_google_scholar():
    webbrowser.open("https://scholar.google.com/")

# 翻訳器のインスタンスを作成
translator = Translator()

# GUIの設定
root = tk.Tk()
root.title("Google Scholar Scraper")

# ウィンドウサイズを1.5倍に設定
root.geometry("1200x600")  # width x height

# カスタムフォントとスタイル
font = ("Helvetica", 12)
bg_color = "#f0f0f0"
button_color = "#4caf50"
button_font = ("Helvetica", 12, "bold")

root.configure(bg=bg_color)

# JSONファイルからキーワードを読み込む
keywords_by_genre = load_keywords_from_json('keywords.json')
genres = list(keywords_by_genre.keys())

# ジャンル選択（オプションメニュー）
tk.Label(root, text="ジャンル:", font=font, bg=bg_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
genre_var = StringVar(root)
genre_var.set(genres[0])  # 初期値として最初のジャンルを設定
genre_menu = OptionMenu(root, genre_var, *genres, command=update_keywords)
genre_menu.config(font=font)
genre_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# キーワード選択（スピンボックス）
tk.Label(root, text="検索キーワード:", font=font, bg=bg_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
keyword_var = StringVar(root)
keywords = keywords_by_genre[genres[0]]
keyword_var.set(keywords[0])
keyword_spinbox = Spinbox(root, values=keywords, textvariable=keyword_var, font=font)
keyword_spinbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# ページ数入力（スピンボックス）
tk.Label(root, text="ページ数:", font=font, bg=bg_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
pages_spinbox = Spinbox(root, from_=1, to=3, font=font)
pages_spinbox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# 発行年入力（スピンボックス）
tk.Label(root, text="発行年（開始）:", font=font, bg=bg_color).grid(row=3, column=0, padx=10, pady=10, sticky="e")
start_year_spinbox = Spinbox(root, from_=1980, to=2024, font=font)
start_year_spinbox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="発行年（終了）:", font=font, bg=bg_color).grid(row=4, column=0, padx=10, pady=10, sticky="e")
end_year_spinbox = Spinbox(root, from_=1980, to=2024, font=font)
end_year_spinbox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# 検索ボタン
search_button = tk.Button(root, text="検索", command=on_search, bg=button_color, fg="white", font=button_font)
search_button.grid(row=5, column=0, columnspan=2, pady=10)

# Google Scholarリンクボタン
gs_link_button = tk.Button(root, text="Open Google Scholar", command=open_google_scholar, bg=button_color, fg="white", font=button_font)
gs_link_button.grid(row=6, column=0, columnspan=2, pady=10)

# 結果表示エリア
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=120, height=30, font=font)
text_area.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
text_area.config(state=tk.DISABLED)

# メインループの開始
root.mainloop()