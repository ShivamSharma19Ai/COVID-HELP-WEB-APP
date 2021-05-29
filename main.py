from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/covid19')
def covid19():
    return render_template('page.html')


@app.route('/vaccinations')
def vaccinations():
    return render_template('vaccinations.html')


app.run(debug=True)
