from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = {
    "mobi-dick": {"id": 1, "author": "Herman Melville", "release_year": 1851},
    "To Kill a Mockingbird": {"id": 2, "author": "Harper Lee", "release_year": 1960}
}

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", books=books)

@app.route('/book/<int:book_id>')
def id(book_id):
    return render_template("book.html", book_id=book_id, books=books)

@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form['title']
        book_id = int(request.form['id'])
        author = request.form['author']
        release_year = int(request.form['release_year'])

        books[title] = {"id": book_id, "author": author, "release_year": release_year}
        return redirect(url_for('home'))

    return render_template('add_book.html')

if __name__ == "__main__":
    app.run(debug=True)
