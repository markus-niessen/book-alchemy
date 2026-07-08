# 📚 Book Alchemy

A web application built with **Flask** and **SQLAlchemy** to manage a personal library of books and authors.

This project was created as part of the **Masterschool Software Engineering** program.

---

## Features

- Add new authors
- Add new books
- Search books by title
- Sort books alphabetically by title
- Sort books alphabetically by author
- View detailed author information
- View detailed book information
- Delete books with confirmation dialog
- Delete authors (including all related books) with confirmation dialog
- Rate books from 1 to 10
- Display book ratings with stars
- Edit book ratings from the book detail page
- Automatic book cover retrieval using ISBN (Open Library Covers API)
- Flash messages for user feedback
- Responsive user interface

### Data Validation

- Duplicate authors are prevented when **name**, **birth date**, and **date of death** are identical.
- Duplicate books are prevented by validating the **ISBN** before saving.
- Every ISBN can only exist once in the database.
- Book ratings are limited to values between **1 and 10**.

---

## Technologies

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- Jinja2
- Open Library Covers API

---

## Project Structure

```text
book-alchemy/
│
├── app.py
├── data_models.py
├── requirements.txt
├── README.md
│
├── data/
│   └── library.sqlite
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── logo.png
│       └── search2.png
│
└── templates/
    ├── home.html
    ├── add_author.html
    ├── add_book.html
    ├── author_detail.html
    └── book_detail.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/markus-niessen/book-alchemy.git
```

Go into the project folder:

```bash
cd book-alchemy
```

Create a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install all required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

or

```bash
flask run --host=0.0.0.0 --port=5002
```

Open your browser:

```text
http://127.0.0.1:5002
```

---

## Database

The project includes a sample SQLite database located at:

```text
data/library.sqlite
```

The sample database contains example authors and books so the application can be explored immediately after cloning the repository.

If you want to start with an empty library, simply delete **only** the file:

```text
data/library.sqlite
```

Do **not** delete the **data** folder.

When the application starts again, a new empty database with the required tables is created automatically.

**Important**

`db.create_all()` only creates missing tables.

It does **not**:

- add missing columns
- modify existing tables
- update the database schema

If the database model changes in the future, the existing database should be recreated or migrated using a migration tool such as Flask-Migrate.

---

## Book Covers

Book covers are automatically retrieved from the **Open Library Covers API** using the ISBN of each book.

If no cover is available for a specific ISBN, no image is displayed.

---

## Future Improvements

- Edit books
- Edit authors
- Sort by publication year
- Sort by rating
- Pagination
- User authentication
- Book descriptions
- Publisher information
- Genre support
- AI-generated book summaries
- AI reading recommendations
- External book reviews
- Book preview or reading sample
- Open Library API integration
- Google Books API integration

---

## Author

**Markus Nießen**

GitHub:
https://github.com/markus-niessen