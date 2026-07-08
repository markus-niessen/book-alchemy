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
- Delete books
- Delete authors (including all related books)
- Rate books from 1 to 10
- Display book ratings with stars
- Edit book ratings from the book detail page
- Automatic book cover retrieval using ISBN (Open Library Covers API)
- Flash messages for user feedback
- Responsive user interface

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

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Database

The application uses a local SQLite database.

Database tables are created automatically when the application is started for the first time.

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