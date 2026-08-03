from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        backend_url = os.getenv(
            "BACKEND_URL",
            "http://backend-service:5000"
        )

        response = requests.get(backend_url)
        data = response.text

        return f"""
        <h1>Hello from Frontend</h1>
        <h2>Backend Response:</h2>
        <pre>{data}</pre>
        """

    except Exception as e:
        return f"""
        <h1>Hello from Frontend</h1>
        <h2>Backend Connection Failed</h2>
        <p>{str(e)}</p>
        """, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
