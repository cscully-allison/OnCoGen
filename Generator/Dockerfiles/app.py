from flask import Flask
from SQLALCHEMY import Base, engine
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    Base.metadata.create_all(engine)
    db = os.environ['DB']

    return db


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
