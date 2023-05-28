from flask import Flask, render_template, jsonify
from database import load_reviews_from_db, load_review_from_db, load_halls_from_db, load_hall_from_db

app = Flask(__name__)


#All Reviews
@app.route("/")
def all_reviews():
  reviews = load_reviews_from_db()
  return render_template('home.html', reviews=reviews)


#All Reviews (API)
@app.route("/api/reviews")
def api_all_reviews():
  reviews = load_reviews_from_db()
  return jsonify(reviews)


#Individual Review
@app.route("/reviews/<id>")
def review(id):
  review = load_review_from_db(id)
  if not review:
    return "Page Not Found", 404
  return render_template('reviewpage.html', review=review)


#All Halls
@app.route("/halls")
def all_halls():
  halls = load_halls_from_db()
  return render_template('halls.html', halls=halls)


#All Halls
@app.route("/api/halls")
def api_all_halls():
  halls = load_halls_from_db()
  return jsonify(halls)


#Individual Hall
@app.route("/halls/<id>")
def hall(id):
  hall = load_hall_from_db(id)
  if not hall:
    return "Page Not Found", 404
  return render_template('hallpage.html', hall=hall)


#Running locally, debug = true
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
