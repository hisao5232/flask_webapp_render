from flaskr import create_app

app = create_app()  # アプリケーションインスタンスを作成

if __name__ == "__main__":
    app.run(debug=True)
