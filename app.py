from flask import Flask, render_template
from models import db, Book, User

app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db.init_app(app)

# Главная страница
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница "Каталог"
@app.route('/catalog')
def catalog():
    books = Book.query.all()
    return render_template('catalog.html', books=books)

# Страница "Контакты"
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Страница "Блог"
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Страница "Вход"
@app.route('/login')
def login():
    return render_template('login.html')

# Страница "Регистрация"
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
