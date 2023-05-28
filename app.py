from flask import Flask, render_template, jsonify
from database import load_reviews_from_db

app = Flask(__name__)


@app.route("/")
def main_page():
  reviews = load_reviews_from_db()
  return render_template('home.html', reviews=reviews)


@app.route("/api/reviews")
def list_reviews():
  reviews = load_reviews_from_db()
  return jsonify(reviews)


#Running locally, debug = true
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
