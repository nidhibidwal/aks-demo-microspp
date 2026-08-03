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

        count = cu*sor.fetchone()[0]

        conn.cl*se()

        return f"Users Count*= {count}"

    except Exception a e:
        return f"Database Erro*: {str(e)}", 500

if __name__ == "*_main__":
    app.run(host="0.0.0.*", port=5000)
