from flask import Flask, render_template, request, redirect, url_for
from pony.orm import db_session, select
from app.database import Book, init_db
from datetime import datetime
from pony.orm import desc 

app = Flask(__name__)
init_db()

@app.route("/")
@db_session
def index():
    zanr_filter = request.args.get("zanr")
    autor_filter = request.args.get("autor")
    sort_by = request.args.get("sort")

    books_query = select(b for b in Book)

    if zanr_filter:
        books_query = books_query.filter(lambda b: b.zanr == zanr_filter)
    if autor_filter:
        books_query = books_query.filter(lambda b: b.autor == autor_filter)

    if sort_by == "naslov":
        books = books_query.order_by(lambda b: b.naslov_knjige)[:]
    elif sort_by == "ocjena":
        books = books_query.order_by(lambda b: b.ocjena)[:]
    else:
        books = books_query.order_by(desc(lambda b: b.vrijeme_dodavanja))[:]

    svi_zanrovi = select(b.zanr for b in Book).distinct()[:]
    svi_autori = select(b.autor for b in Book).distinct()[:]

    return render_template(
        "index.html",
        books=books,
        zanrovi=svi_zanrovi,
        autori=svi_autori,
        zanr_filter=zanr_filter,
        autor_filter=autor_filter,
        sort_by=sort_by
    )


@app.route("/add", methods=["GET", "POST"])
@db_session
def add_book():
    if request.method == "POST":
        naslov = request.form["naslov_knjige"]
        autor = request.form["autor"]
        zanr = request.form["zanr"]
        ocjena = int(request.form["ocjena"])
        biljeske = request.form.get("biljeske", "")

        Book(
            naslov_knjige=naslov,
            autor=autor,
            zanr=zanr,
            ocjena=ocjena,
            biljeske=biljeske,
            vrijeme_dodavanja=datetime.now()
        )
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/delete/<int:book_id>", methods=["POST"])
@db_session
def delete_book(book_id):
    book = Book.get(id=book_id)
    if book:
        book.delete()
    return redirect(url_for("index"))

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
@db_session
def edit_book(book_id):
    book = Book.get(id=book_id)
    if not book:
        return "Knjiga nije pronađena", 404

    if request.method == "POST":
        book.naslov_knjige = request.form["naslov_knjige"]
        book.autor = request.form["autor"]
        book.zanr = request.form["zanr"]
        book.ocjena = int(request.form["ocjena"])
        book.biljeske = request.form.get("biljeske", "")
        return redirect(url_for("index"))

    return render_template("edit.html", book=book)
