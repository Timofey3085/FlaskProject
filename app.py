from datetime import datetime
from functools import wraps

import pytest
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect, FlaskForm
from werkzeug import Response
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import Form, StringField, PasswordField, validators
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.secret_key = '1234567890'

db: SQLAlchemy = SQLAlchemy(app)
csrf: CSRFProtect = CSRFProtect(app)

login_manager: LoginManager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    submit = SubmitField('Login')


class RegistrationForm(Form):
    email: StringField = StringField('Email', [validators.Length(min=6, max=100), validators.Email()])
    password: PasswordField = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6)])
    submit = SubmitField('Register')


class Article(db.Model):
    id: db.Column = db.Column(db.Integer, primary_key=True)
    title: db.Column = db.Column(db.String(100), nullable=False)
    description: db.Column = db.Column(db.String(200))
    created_at: db.Column = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: db.Column = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Article %r>' % self.id


class User(UserMixin, db.Model):
    id: db.Column = db.Column(db.Integer, primary_key=True)
    email: db.Column = db.Column(db.String(100), unique=True, nullable=False)
    password: db.Column = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return '<User %r>' % self.email


@app.route('/register', methods=['GET', 'POST'])
@csrf.exempt
def register() -> Response | str:
    """Регистрация нового пользователя"""
    form: RegistrationForm = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        email: str = form.email.data
        password: str = generate_password_hash(form.password.data)

        new_user: User = User(email=email, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)  # Вход пользователя после регистрации
            return redirect(url_for('list'))
        except Exception as e:
            return f"Ошибка при регистрации пользователя: {str(e)}"

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@csrf.exempt
def login() -> Response | str:
    """Авторизация пользователя"""
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        email = form.username.data
        password = form.password.data

        user: User = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Добро пожаловать, {}!'.format(user.email), 'info')
            return redirect('/tasks/list')
        else:
            flash('Неверный email или пароль.', 'error')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout() -> Response:
    """Выход пользователя"""
    logout_user()
    return redirect('/tasks/list')


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(int(user_id))


def login_required_with_redirect(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        """Декоратор для проверки авторизации пользователя"""
        if not current_user.is_authenticated:
            return redirect(url_for('login', next=request.url))  # Переадресация на страницу login.html
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def index() -> Response:
    """Главная страница"""
    return redirect('/tasks/list')


@app.route('/', methods=['POST'])
@app.route('/tasks')
@login_required_with_redirect
def create() -> Response | str:
    """Создание новой задачи"""
    if request.method == "POST":
        title: str = request.form['title']
        description: str = request.form['description']

        article: Article = Article(title=title, description=description)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/tasks/list')
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"
    else:
        return render_template('create.html')


@app.route('/tasks/list', methods=['GET'])
def list() -> str:
    """Список всех задач"""
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('list.html', articles=articles)


@app.route('/tasks/info/<int:id>', methods=['GET'])
def info(id: int) -> str:
    """Просмотр информации о задаче"""
    article: Article = Article.query.get_or_404(id)
    return render_template('info.html', article=article)


@app.route('/tasks/update/<int:id>', methods=['GET', 'POST'])
@login_required_with_redirect
def update(id: int) -> Response | str:
    """Обновление задачи"""
    article: Article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.description = request.form['description']
        article.updated_at = datetime.utcnow()

        try:
            db.session.commit()
            return redirect('/tasks/list')
        except:
            return "Произошла ошибка при обновлении записи"

    return render_template('update.html', article=article)


@app.route('/tasks/delete/<int:id>', methods=['GET', 'POST'])
@login_required_with_redirect
def delete(id: int) -> Response | str:
    """Удаление задачи"""
    article: Article = Article.query.get_or_404(id)

    if request.method == 'POST':
        if request.form.get('confirm') == "confirm":
            try:
                db.session.delete(article)
                db.session.commit()
                flash('Задача успешно удалена', 'success')  # Добавляем сообщение об успешном удалении
                return redirect('/tasks/list')
            except:
                flash('Произошла ошибка', 'danger')  # Добавляем сообщение об ошибке
    return render_template('delete.html', article=article)


def test_info_page():
    """Тест на проверку страницы с информацией о задаче"""
    with app.test_client() as client:
        response = client.get('/tasks/info/1')
        assert response.status_code == 200  # Проверяем статус код ответа, должен быть 200


if __name__ == '__main__':
    app.run(debug=True)
    pytest.main()
