MODE = "DEVELOPMENT"
FLASK_SECRET_KEY = "dev"

# SQL
# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = "postgres://psql:psql@localhost:5432/bills"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_RECORD_QUERIES = True
