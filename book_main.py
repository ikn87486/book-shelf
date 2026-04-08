import book_db

def main():
    book_db.create_table()
    user_select = input("add or delete >> ")

    if user_select == "add":
        user_input = input("追加する本の名前")
        book_db.add_book(user_input)

        print(f"「{user_input}」をデータベースに追加しました！")

        print("--- 実行後のデータベースの中身 ---")
        books_data = book_db.get_book()
        for row in books_data:
            print(f"ID: {row[0]}, 作品名: {row[1]}, 追加日: {row[2]}")
    
    elif user_select == "delete":
        print("--- 実行前のデータベースの中身 ---")
        books_data = book_db.get_book()
        for row in books_data:
            print(f"ID: {row[0]}, 作品名: {row[1]}, 追加日: {row[2]}")

        user_input = input("削除する本のid")
        book_db.delete_book(user_input)

        print(f"「{user_input}」をデータベースから削除しました！")

        print("--- 実行後のデータベースの中身 ---")
        books_data = book_db.get_book()
        for row in books_data:
            print(f"ID: {row[0]}, 作品名: {row[1]}, 追加日: {row[2]}")
    else:
        print("入力が正しくありません")


        


    

# このファイルが実行された時だけmain()を動かす
if __name__ == "__main__":
    main()