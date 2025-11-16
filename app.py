'''from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>'''


from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('main.html')

@app.route('/about')
def about():
    return "Страница о нас"

if __name__ == '__main__':
    app.run(debug=True)
