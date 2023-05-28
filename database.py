from sqlalchemy import create_engine, text
import os

#Authentication & Setting Up Connection
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert/pem"
                       }})


#Load all reviews
def load_reviews_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text(
        "SELECT * FROM reviews LEFT JOIN halls ON reviews.hallId=halls.hallId;"
      ))
    result_all = result.all()
    column_name = result.keys()
    reviews = []
    for row in result_all:
      reviews.append(dict(zip(column_name, row)))
    return reviews


#Load a review based on id
def load_review_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM reviews WHERE reviewId={id}"))
    rows = []
    column_name = result.keys()
    for row in result.all():
      rows.append(dict(zip(column_name, row)))

    if len(rows) == 0:
      return None
    else:
      return (rows[0])


#Load all halls
def load_halls_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM halls"))
    result_all = result.all()
    column_name = result.keys()
    halls = []
    for row in result_all:
      halls.append(dict(zip(column_name, row)))
    return halls

#Load a hall details
def load_hall_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM halls WHERE hallId={id}"))
    rows = []
    column_name = result.keys()
    for row in result.all():
      rows.append(dict(zip(column_name, row)))

    if len(rows) == 0:
      return None
    else:
      return (rows[0])