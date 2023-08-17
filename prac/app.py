from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pagination.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    name = db.Column(db.String)
    address = db.Column(db.String)

    def __str__(self):
        return self.title

@app.route("/")
def thread():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
