from flask import Flask
import pymysql
import os

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        port=3306,
    )


@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        conn.close()
        return f"Users Count = {count}"

    except Exception as e:
        return f"Database Error: {str(e)}", 500


@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.route("/ready")
def ready():
    try:
        conn = get_db_connection()
        conn.ping(reconnect=True)
        conn.close()
        return {"status": "ready"}, 200
    except Exception as e:
        return {"status": "not_ready", "error": str(e)}, 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
