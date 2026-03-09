from flask import Flask
from flask import request, redirect, url_for, render_template
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    )

app = Flask(__name__) # Создание приложения

# @app.route("/") # Определение маршрута для главной страницы
# def home():
#     return "Привет, Flask!"

# @app.route("/")
# def home():
#     return redirect(url_for('profile', username='Гость'))



@app.route("/")
def home():
    app.logger.info("Главная страница открыта")
    return render_template('index.html', name='Админ')


@app.route('/about')
def about():
    return "Эта страница 'О нас!'. "

@app.route('/contact')
def contact():
    return "Контакт: Ежик123@yandex.ru"

@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}!'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Данные отправлены!"
    return "Отобразить форму"

@app.route('/post/<int:post_id>')
def post(post_id):
    return f'Вы просматривает пост № {post_id}'

@app.route('/search')
def search():
    query = request.args.get('query', 'Ничего не найдено')
    return f'Вы искали: {query}'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f' Привет, {username}! Вы успешно вошли в систему!'

@app.errorhandler(404)
def page_not_found(error):
    return "Страница не найдена!", 404


@app.route('/users')
def users():
    user_list = ['Андрей','Кирил','Олег']
    return render_template('users.html', user=user_list)

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(f'Ошибка 500: {error}')
    return "Ошибка сервера. Попробуйте позже.", 500

@app.errorhandler(403)
def forbidden(error):
    return "Доступ запрещен", 403

@app.errorhandler(400)
def bad_request(error):
    return "Некорректный запрос.", 400

@app.before_request
def log_request():
    app.logger.info(f"Запрос: {request.method} {request.url}")

handler = RotatingFileHandler("server.log", maxBytes=100000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)


if __name__ == '__main__':
    app.run(debug=True) # Запуск сервера в режиме отладки
