from flask import Flask, request, render_template_string
from lms import LibraryManagementSystem

app = Flask(__name__)

# Initialize the LMS with the database
lms = LibraryManagementSystem("lms_database")

@app.route('/checkout', methods=['POST'])
def checkout():
    book_id = request.args.get('bookId')
    borrower_id = request.args.get('borrowerId')
    result = lms.checkout_book(borrower_id, book_id)
    return render_template_string(f"<html><body><pre>{result}</pre></body></html>")

@app.route('/return', methods=['POST'])
def return_book():
    book_id = request.args.get('bookId')
    borrower_id = request.args.get('borrowerId')
    result = lms.return_book(borrower_id, book_id)
    return render_template_string(f"<html><body><pre>{result}</pre></body></html>")

@app.route('/reset', methods=['POST'])
def reset():
    result = lms.reset_database()
    return render_template_string(f"<html><body><pre>{result}</pre></body></html>")

@app.route('/books', methods=['GET'])
def books():
    result = lms.display_books()
    books = result.splitlines()  # Split the result by lines
    book_entries = "".join([f"<pre>{book}</pre>" for book in books])  # Wrap each book in its own <pre> tag
    return render_template_string(f"<html><body>{book_entries}</body></html>")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
