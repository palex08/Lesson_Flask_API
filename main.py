from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    quote_data = get_random_quote()
    if quote_data:
        quote = quote_data['content']
        author = quote_data['author']
    else:
        quote = "Oops! Couldn't fetch the quote."
        author = "Unknown"

    return render_template('index.html', quote=quote, author=author)

@app.route('/new_quote')
def new_quote():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
