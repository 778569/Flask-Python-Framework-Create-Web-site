from flask import Flask

app = Flask(__name__)
# print(__name__)
@app.route('/')
def home():
    return "Hello Flask!"

@app.route('/about')
def about():
    return "This is url shortener..!"

if __name__ == '__main__':
    app.run()
