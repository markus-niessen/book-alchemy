# 📚 Book Alchemy

A web application built with **Flask** and **SQLAlchemy** to manage a personal library of books and authors.

This project was created as part of the **Masterschool Software Engineering** program.

---

## Features

- Add new authors
- Add new books
- Search books by title
- View detailed author information
- View detailed book information
- Delete books
- Delete authors (including all related books)
- Automatic book cover retrieval using ISBN (Open Library)
- Rate books from 1 to 10
- Display book ratings with stars
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

---

## Project Structure

```
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

Create a virtual environment:

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

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Database

The application uses a local SQLite database.

Tables are created automatically when the application is started for the first time.

---

## Book Covers

Book covers are automatically retrieved from the **Open Library Covers API** using the ISBN of each book.

---

## Future Improvements

- Edit books
- Edit authors
- Sort by publication year
- Sort by rating
- Pagination
- User authentication

---

## Author

**Markus Nießen**

GitHub:
https://github.com/markus-niessen