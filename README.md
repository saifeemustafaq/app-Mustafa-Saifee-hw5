# Library Management System (LMS) Project Setup

1. Make sure you are in the project root directory

2. Create a virtual environment and activate it:

```commandline
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:

```commandline
pip install -r requirements.txt
```

4. Start the Flask server:

```commandline
python app.py
```

The server will be live on: http://localhost:8080/

Example calls:

> [!NOTE]  
> POST requests like `checkout`, `reset`, and `return` might not work on browsers, since the browser treats them as `GET` requests.

http://localhost:8080/checkout?borrowerId=L34&bookId=A312

http://localhost:8080/return?borrowerId=L34&bookId=A312

http://localhost:8080/books

http://localhost:8080/reset

Make sure you have MongoDB installed and running on your local machine.