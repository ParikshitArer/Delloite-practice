from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Cloud Application</title>
    </head>
    <body>
        <h1>Azure Cloud Application</h1>
        <h2>Project 2 - Azure App Service</h2>
        <p>Running on Azure App Service</p>
        <p>Linux + Python + Flask + Gunicorn</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)