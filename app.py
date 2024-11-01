from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal buku (total 15) dengan detail lebih lengkap
books = {
    "1": {
        "title": "Atomic Habits",
        "author": "James Clear",
        "quantity": 50,
        "price": 200000,
        "publisher": "Avery",
        "publication_date": "2018-10-16",
        "category": "Self-help"
    },
    "2": {
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "quantity": 30,
        "price": 180000,
        "publisher": "Crown Publishing",
        "publication_date": "2011-09-13",
        "category": "Business"
    },
    "3": {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "quantity": 25,
        "price": 250000,
        "publisher": "Harper",
        "publication_date": "2015-02-10",
        "category": "History"
    },
    "4": {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "quantity": 40,
        "price": 220000,
        "publisher": "Farrar, Straus and Giroux",
        "publication_date": "2011-10-25",
        "category": "Psychology"
    },
    "5": {
        "title": "Educated",
        "author": "Tara Westover",
        "quantity": 35,
        "price": 190000,
        "publisher": "Random House",
        "publication_date": "2018-02-20",
        "category": "Memoir"
    },
    "6": {
        "title": "The Power of Habit",
        "author": "Charles Duhigg",
        "quantity": 45,
        "price": 210000,
        "publisher": "Random House",
        "publication_date": "2012-02-28",
        "category": "Self-help"
    },
    "7": {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "quantity": 55,
        "price": 150000,
        "publisher": "HarperOne",
        "publication_date": "2016-09-13",
        "category": "Self-help"
    },
    "8": {
        "title": "Becoming",
        "author": "Michelle Obama",
        "quantity": 60,
        "price": 280000,
        "publisher": "Crown",
        "publication_date": "2018-11-13",
        "category": "Memoir"
    },
    "9": {
        "title": "Principles",
        "author": "Ray Dalio",
        "quantity": 33,
        "price": 240000,
        "publisher": "Simon & Schuster",
        "publication_date": "2017-09-19",
        "category": "Business"
    },
    "10": {
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "quantity": 70,
        "price": 120000,
        "publisher": "Simon & Schuster",
        "publication_date": "1936-10-01",
        "category": "Self-help"
    },
    "11": {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "quantity": 50,
        "price": 160000,
        "publisher": "Free Press",
        "publication_date": "1989-08-15",
        "category": "Self-help"
    },
    "12": {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "quantity": 45,
        "price": 100000,
        "publisher": "Oxford University Press",
        "publication_date": "2005-07-01",
        "category": "Military strategy"
    },
    "13": {
        "title": "Outliers",
        "author": "Malcolm Gladwell",
        "quantity": 28,
        "price": 180000,
        "publisher": "Little, Brown and Company",
        "publication_date": "2008-11-18",
        "category": "Psychology"
    },
    "14": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "quantity": 65,
        "price": 140000,
        "publisher": "Little, Brown and Company",
        "publication_date": "1951-07-16",
        "category": "Fiction"
    },
    "15": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "quantity": 55,
        "price": 175000,
        "publisher": "J.B. Lippincott & Co.",
        "publication_date": "1960-07-11",
        "category": "Fiction"
    }
}

# Classes for CRUD functionality as in previous example
class BookList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(books),
            "books": books
        }

class BookDetail(Resource):
    def get(self, book_id):
        if book_id in books:
            return {
                "error": False,
                "message": "Success",
                "book": books[book_id]
            }
        return {"error": True, "message": "Book not found"}, 404

class AddBook(Resource):
    def post(self):
        data = request.get_json()
        book_id = str(len(books) + 1)
        new_book = {
            "title": data.get("title"),
            "author": data.get("author"),
            "quantity": data.get("quantity"),
            "price": data.get("price"),
            "publisher": data.get("publisher"),
            "publication_date": data.get("publication_date"),
            "category": data.get("category")
        }
        books[book_id] = new_book
        return {
            "error": False,
            "message": "Book added successfully",
            "book": new_book
        }, 201

class UpdateBook(Resource):
    def put(self, book_id):
        if book_id in books:
            data = request.get_json()
            book = books[book_id]
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])
            book["quantity"] = data.get("quantity", book["quantity"])
            book["price"] = data.get("price", book["price"])
            book["publisher"] = data.get("publisher", book["publisher"])
            book["publication_date"] = data.get("publication_date", book["publication_date"])
            book["category"] = data.get("category", book["category"])
            return {
                "error": False,
                "message": "Book updated successfully",
                "book": book
            }
        return {"error": True, "message": "Book not found"}, 404

class DeleteBook(Resource):
    def delete(self, book_id):
        if book_id in books:
            deleted_book = books.pop(book_id)
            return {
                "error": False,
                "message": "Book deleted successfully",
                "book": deleted_book
            }
        return {"error": True, "message": "Book not found"}, 404

api.add_resource(BookList, '/books')
api.add_resource(BookDetail, '/books/<string:book_id>')
api.add_resource(AddBook, '/books/add')
api.add_resource(UpdateBook, '/books/update/<string:book_id>')
api.add_resource(DeleteBook, '/books/delete/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
