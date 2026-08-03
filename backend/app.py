from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"],
            port=3306
        )

        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")

        count = cursor.fetchone()[0]

        conn.close()

        return f"Users Count = {count}"

    except Exception as e:
        return f"Database Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
