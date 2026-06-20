from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body style="background:#28a745;color:white;text-align:center;padding-top:200px;font-size:50px;">
    🟢 GREEN ENVIRONMENT V2
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
