import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from data_models import db, Author, Book

app = Flask(__name__)
app.secret_key = "my_secret_key"

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_query = request.args.get("search", "")
    sort_by = request.args.get("sort", "")

    query = Book.query

    if search_query:
        query = query.filter(Book.title.ilike(f"%{search_query}%"))

    if sort_by == "title":
        query = query.order_by(Book.title.asc())
    elif sort_by == "author":
        query = query.join(Author).order_by(Author.name.asc())
    else:
        query = query.order_by(Book.id.asc())

    books = query.all()

    return render_template(
        "home.html",
        books=books,
        search_query=search_query,
        sort_by=sort_by
    )


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    message = None

    if request.method == "POST":
        name = request.form.get("name")
        birth_date = request.form.get("birth_date")
        date_of_death = request.form.get("date_of_death")

        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        if date_of_death:
            date_of_death = datetime.strptime(
                date_of_death,
                "%Y-%m-%d"
            ).date()
        else:
            date_of_death = None

        existing_author = Author.query.filter_by(
            name=name,
            birth_date=birth_date,
            date_of_death=date_of_death
        ).first()

        if existing_author:
            message = "Author already exists."
        else:
            new_author = Author(
                name=name,
                birth_date=birth_date,
                date_of_death=date_of_death
            )

            db.session.add(new_author)
            db.session.commit()

            message = "Author successfully added."

    return render_template("add_author.html", message=message)


@app.route("/author/<int:author_id>/delete", methods=["POST"])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)

    db.session.delete(author)
    db.session.commit()

    flash(f"Author '{author.name}' and all related books were deleted successfully.")
    return redirect(url_for("home"))


@app.route("/author/<int:author_id>")
def author_detail(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template("author_detail.html", author=author)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    message = None
    authors = Author.query.order_by(Author.name).all()

    if request.method == "POST":
        title = request.form.get("title")
        isbn = request.form.get("isbn")
        publication_year = request.form.get("publication_year")
        rating = request.form.get("rating")
        author_id = request.form.get("author_id")

        existing_book = Book.query.filter_by(isbn=isbn).first()

        if existing_book:
            message = "A book with this ISBN already exists."
        else:
            new_book = Book(
                title=title,
                isbn=isbn,
                publication_year=publication_year,
                rating=int(rating) if rating else None,
                author_id=author_id
            )

            db.session.add(new_book)
            db.session.commit()

            message = "Book successfully added."

    return render_template(
        "add_book.html",
        authors=authors,
        message=message
    )


@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author = book.author

    db.session.delete(book)
    db.session.commit()

    if author and len(author.books) == 0:
        db.session.delete(author)
        db.session.commit()

    flash("Book successfully deleted.")

    return redirect(url_for("home"))


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book_detail.html", book=book)


@app.route("/rate_book/<int:book_id>", methods=["POST"])
def rate_book(book_id):
    book = Book.query.get_or_404(book_id)
    rating = request.form.get("rating")

    if rating:
        rating = int(rating)

        if 1 <= rating <= 10:
            book.rating = rating
            db.session.commit()
            flash("Book rating saved successfully.")
        else:
            flash("Rating must be between 1 and 10.")

    return redirect(url_for("book_detail", book_id=book.id))


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5002, debug=True)
