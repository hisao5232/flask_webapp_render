from . import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)               # インデックスとなるユニークな値
    title = db.Column(db.String(100), nullable=False)          # タスクのタイトル
    description = db.Column(db.Text, nullable=True)            # タスクの詳細
    due_date = db.Column(db.DateTime, nullable=True)           # タスクの期限

    def __repr__(self):
        return f'<Todo {self.title}, Due: {self.due_date}>'