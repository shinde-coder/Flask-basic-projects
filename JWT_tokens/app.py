from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e51eea5e1bde4078822b42e84887d6e2'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://127.0.0.1:5000/route?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2hpbmRlIiwiZXhwIjoxNjkyMTYxNDEzfQ.uKUkrB5VzPD-j3KPJTmDAbjlG2BKmZBJgwl8OiHnWuo

        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'Message': 'Token has expired'}), 403
        except jwt.DecodeError:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently'

@app.route('/public')
def public():
    return 'For Public'

@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard!'

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'shinde' and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            'exp': datetime.utcnow() + timedelta(seconds=120)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed"'})

if __name__ == "__main__":
    app.run(debug=True)
