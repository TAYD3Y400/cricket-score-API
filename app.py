from flask import Flask, jsonify
from cricket_scraper import scrape_cricket_data


app = Flask(__name__)


@app.route('/')
def cricgfg():
    url = 'https://sports.ndtv.com/cricket/live-scores'
    result = scrape_cricket_data(url)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
