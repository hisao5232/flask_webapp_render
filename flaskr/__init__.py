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

    DATABASE_URL = os.getenv("DATABASE_URL")

    # Flask SQLAlchemy 設定
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
