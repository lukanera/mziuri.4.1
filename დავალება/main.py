from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("hello.html")


@app.route('/aboutus')
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<name>/<int:age>')
def profile(name, age):
    return render_template("index.html", my_name=name, my_age=age)


@app.route('/again')
def again():
    return render_template("again.html")


if __name__ == "__main__":
    app.run(debug=True)