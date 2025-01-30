from flask import render_template, request, redirect, url_for
from . import db
from .models import Todo
from datetime import datetime

def register_routes(app):
# トップページの表示
    @app.route('/')
    def index():
        """ タスク一覧を表示"""
        todos = Todo.query.order_by(Todo.due_date).all()
        return render_template('index.html', todos=todos)

# タスク追加ページの表示
    @app.route('/add', methods=['GET', 'POST'])
    def add_todo():
        """POSTの場合（タスク追加フォームを送信時）"""
        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            due_date_str = request.form.get('due_date')

            # 空チェック
            if not title.strip():  
                return "Title is required!", 400

            # 日付を変換（空の場合はNone）
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None

            new_todo = Todo(title=title, description=description, due_date=due_date)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for('index'))

        """GETの場合（タスク追加フォームを表示したい時）"""
        return render_template('add.html')  

# タスク削除のデータベース操作
    @app.route('/delete/<int:todo_id>')
    def delete_todo(todo_id):
        """指定したIDのタスクを削除"""
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))

# タスク編集のページ表示
    @app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
    def update_todo(todo_id):
        """POSTの場合（指定したIDのタスクを編集）"""
        todo = Todo.query.get_or_404(todo_id)
        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            due_date_str = request.form.get('due_date')

            # 空チェック
            if not title.strip():  
                return "Title is required!", 400

            todo.title = title
            todo.description = description
            todo.due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None

            db.session.commit()
            return redirect(url_for('index'))
        """GETの場合（編集用フォームを表示）"""
        return render_template('update.html', todo=todo)  

# 必ず最後にこの関数を呼び出す
def init_views(app):
    register_routes(app)