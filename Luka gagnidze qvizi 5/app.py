from flask import Flask, render_template, url_for
app = Flask(__name__)

task = ["დაალაგე სახლი", "იმეცადინე", "დაისვენე", "ჭამე"]

@app.route('/')
def home():
    return render_template("index.html", task = task)

@app.route('/add_task')
def add_task():
    return render_template("add_task.html", task = task)

if __name__ == "__main__":
    app.run(debug=True)