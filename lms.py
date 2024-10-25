import pymongo
from pymongo import MongoClient
import sys

class LibraryManagementSystem:
    def __init__(self, database_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database_name]
        self.books_collection = self.db['books']
        self.borrowers_collection = self.db['borrowers']
        self.reset_database()

    def reset_database(self):
        # Clear existing data
        self.books_collection.delete_many({})
        self.borrowers_collection.delete_many({})

        # Insert initial books data
        books = [
            {"_id": "A234", "title": "The 101 Dalmations", "author": "Dodie Smith", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "A675", "title": "The Adventures of Huckleberry Finn", "author": "Mark Twain", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "A212", "title": "Bag of Bones", "author": "Stephen King", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "B671", "title": "Charlie and the Chocolate Factory", "author": "Roald Dahl", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "B534", "title": "Charlotte's Web", "author": "E.B.White", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "B777", "title": "A Christmas Carol", "author": "Charles Dickens", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "B778", "title": "Dracula", "author": "Bram Stoker", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "B812", "title": "A Farewell to Arms", "author": "Ernest Hemingway", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "C101", "title": "The Firm", "author": "John Grisham", "checked_out": False, "borrower_id": "", "borrower_name": ""},
            {"_id": "C102", "title": "War and Peace", "author": "Leo Tolstoy", "checked_out": False, "borrower_id": "", "borrower_name": ""}
        ]
        self.books_collection.insert_many(books)

        # Insert initial borrowers data
        borrowers = [
            {"_id": "L34", "name": "Andrea Selleck", "phone": "639-555-1239"},
            {"_id": "L22", "name": "Lucas Hyatt", "phone": "408-555-2365"},
            {"_id": "L19", "name": "Carol Leonard", "phone": "650-555-8921"},
            {"_id": "L84", "name": "Ayesha Ford", "phone": "415-555-2120"},
            {"_id": "L77", "name": "Kenneth Trout", "phone": "510-555-1982"}
        ]
        self.borrowers_collection.insert_many(borrowers)

        return "Database has been reset successfully"

    def checkout_book(self, borrower_id, book_id):
        borrower = self.borrowers_collection.find_one({"_id": borrower_id})
        if not borrower:
            return f"Borrower with ID {borrower_id} does not exist."

        book = self.books_collection.find_one({"_id": book_id})
        if not book:
            return f"Book with ID {book_id} does not exist."

        if book["checked_out"]:
            return f"'{book['title']}' is already checked out by someone."

        self.books_collection.update_one(
            {"_id": book_id},
            {"$set": {"checked_out": True, "borrower_id": borrower_id, "borrower_name": borrower["name"]}}
        )
        return f"'{borrower['name']}' has checked out '{book['title']}'"

    def return_book(self, borrower_id, book_id):
        borrower = self.borrowers_collection.find_one({"_id": borrower_id})
        if not borrower:
            return f"Borrower with ID {borrower_id} does not exist."

        book = self.books_collection.find_one({"_id": book_id})
        if not book:
            return f"Book with ID {book_id} does not exist."

        if not book["checked_out"] or book["borrower_id"] != borrower_id:
            return f"'{borrower['name']}' has not currently checked out '{book['title']}'"

        self.books_collection.update_one(
            {"_id": book_id},
            {"$set": {"checked_out": False, "borrower_id": "", "borrower_name": ""}}
        )
        return f"'{borrower['name']}' has returned '{book['title']}'"

    def display_books(self):
        books = self.books_collection.find()
        result = "book_id,title,author,checked_out,borrower_id,borrower_name\n"
        for book in books:
            checked_out = "Y" if book["checked_out"] else "N"
            result += f"{book['_id']},\"{book['title']}\",\"{book['author']}\",\"{checked_out}\",\"{book['borrower_id']}\",\"{book['borrower_name']}\"\n"
        return result