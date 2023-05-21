from flask import Flask, render_template, jsonify

app = Flask(__name__)

REVIEWS = [{
  'id': 1,
  'hall': "Kent Ridge Hall",
  'rating': '4/5',
  'title': "Amazing Hall",
  "content": "Great location! Really near to the NUS Business School"
}, {
  'id': 2,
  'hall': "Raffles Hall",
  'rating': '4.5/5',
  'title': "Great Experience",
  "content": "Good facilities. Gym newly renovated!"
}, {
  'id': 3,
  'hall': "Temasek Hall",
  'rating': '3.8/5',
  'title': "Really bad experience",
  "content": "Near to supper streatch. Amazing CCAs"
}]


@app.route("/")
def main_page():
  return render_template('home.html', reviews=REVIEWS)


@app.route("/api/reviews")
def list_reviews():
  return jsonify(REVIEWS)


#Running locally, debug = true
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
