from flask import Flask, render_template, request, redirect
import book_db

app = Flask(__name__)

# アプリ起動時に、念のためテーブルを準備しておく
book_db.create_table()

@app.route("/")
def index():
    # 1. 裏側の機能を使って、データベースから本の一覧を取得
    books_data = book_db.get_book()
    return render_template("index.html", books = books_data)

@app.route("/add", methods=["POST"])
def add():
    user_input = request.form["book_name"]
    book_db.add_book(user_input)

    return redirect("/")
# このファイルが実行されたら、Webサーバーを起動する
if __name__ == "__main__":
    app.run(debug=True)