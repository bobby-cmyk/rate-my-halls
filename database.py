from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert/pem"
                       }})


def load_reviews_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from reviews"))
    result_all = result.all()
    column_name = result.keys()
    reviews = []
    for row in result_all:
      reviews.append(dict(zip(column_name, row)))
    return reviews
