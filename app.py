from main.routes import app
from main import db


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)