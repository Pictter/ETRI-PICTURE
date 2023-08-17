from flask import Flask, request, render_template
from ChatGPT import ChatGPT

app = Flask(__name__)

@app.route('/')
def root():
    return "hello world!"

@app.route('/user')
def index():
    return render_template("main.html")

@app.route('/letter', methods=['POST'])
def result():
    letter = request.form.get('letter')
    keyword = ChatGPT(letter)
    return render_template("letter.html",keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)