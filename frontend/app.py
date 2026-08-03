from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get(
            os.environ["BACKEND_URL"]
        )

        return f"""
        <h1>Hello from Frontend</h1>
        <h2>{response.text}</h2>
        """

    except Exception as e:
        return f"Backend Connection Failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
