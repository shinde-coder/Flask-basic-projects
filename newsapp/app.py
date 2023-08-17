from flask import *
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3cac7692917746e89fed487749aac232'
    r = requests.get(url).json()

    cases = {
        'articles' : r['articles']
    }

    return render_template('index.html', cases=cases)

if __name__=="__main__":
    app.run(debug=True)
