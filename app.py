from flask import Flask
import book_db

app = Flask(__name__)

# アプリ起動時に、念のためテーブルを準備しておく
book_db.create_table()

@app.route("/")
def index():
    # 1. 裏側の機能を使って、データベースから本の一覧を取得
    books_data = book_db.get_book()
    
    # 2. ブラウザに表示するための「文字」を組み立てる
    result_text = "<h1>登録されている本の一覧</h1>"
    
    for row in books_data:
        # <p> は段落（改行）を表す簡単な目印です
        result_text += f"<p>ID: {row[0]} / 作品名: {row[1]}</p>"
        
    # 3. 組み立てた文字をブラウザに返す！
    return result_text

# このファイルが実行されたら、Webサーバーを起動する
if __name__ == "__main__":
    app.run(debug=True)