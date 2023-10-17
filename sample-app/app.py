from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<title>Hello, World!</title>"

if __name__ == "__main__":
    app.run(debug=True)