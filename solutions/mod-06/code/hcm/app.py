# app.py
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the HCM Application'


# login function
@app.route('/login', methods=['POST'])
def login():
    credentials = request.data
    # logic here (e.g., check credentials in a database)
    if credentials == b'{"email": "labs", "password": "Pytest.Labs_4ALL"}':
        return b'Successful login'  # For demonstration purposes
    else:
        return b'Failed login'


if __name__ == 'hcm-app':
    app.run(debug=True)
