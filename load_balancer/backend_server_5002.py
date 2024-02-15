# backend_server_5002.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print(f"hello from backend server 5002")
    return 'Hello from Backend Server 5002!'

if __name__ == '__main__':
    app.run(port=5002)