from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/covid19')
def covid19():
    return render_template('page.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')


app.run(debug=True)
