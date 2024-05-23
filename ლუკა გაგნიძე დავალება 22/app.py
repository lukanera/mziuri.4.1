from flask import Flask, render_template, request, url_for, session, redirect
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "kumesta"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        session["user"] = user
        return redirect(url_for("home"))
    return render_template('login.html')


@app.route('/')
def i():
    if "user" in session:
        return redirect("home")
    return redirect(url_for("login"))


@app.route("/home")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("home.html", user=user)


@app.route("/logout")
def logout():
    text = "You are logged out"
    session.pop("user", None)
    return render_template("home.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)