from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    # 環境変数を読み込む
    load_dotenv()
    
    app = Flask(__name__)

    # sqlite接続設定
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 環境変数 `DATABASE_URL` から接続情報を取得
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Internal Database URL を使用するために `sslmode=require` を確認
    if DATABASE_URL and "sslmode" not in DATABASE_URL:
        DATABASE_URL += "?sslmode=require"

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # PostgreSQL接続設定
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import models, views  # viewsをインポート
        views.init_views(app)       # ルートを登録
        db.create_all()             # テーブルを作成

    return app
