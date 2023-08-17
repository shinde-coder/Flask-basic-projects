# from flask import *
# import requests

# app = Flask(__name__)
# #&with_original_language=ka
# @app.route("/")
# def home():
#     url = 'https://api.themoviedb.org/3/discover/movie?api_key=7cfa89984bd144f23abc775b8be1ba68'
#     r = requests.get(url).json()

#     cases = {
#         'results' : r['results']
#     }

#     return render_template('index.html', cases=cases)

# if __name__=="__main__":
#     app.run(debug=True)
#here the searching functionality is not working
from flask import Flask, request, render_template
import requests

app = Flask(__name__)


#base_url = 'https://api.themoviedb.org/3/search/movie'
#url = f"{base_url}?api_key={api_key}&query={search_query}&with_original_language=te"
#url = 'https://api.themoviedb.org/3/discover/movie?api_key=7cfa89984bd144f23abc775b8be1ba68&query={search_query}'


def fetch_movies(search_query=""):
    api_key = "7cfa89984bd144f23abc775b8be1ba68"
    language=''
    if search_query:
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={search_query}&with_original_language={language}'
    else:
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_original_language={language}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results")
    else:
        results = []
    return results

@app.route("/", methods=["GET"])
def home():
    search_query = request.args.get("search", "")
    movies = fetch_movies(search_query)
    cases = {
        'results': movies
    }
    return render_template('index.html', cases=cases)

if __name__ == "__main__":
    app.run(debug=True)
