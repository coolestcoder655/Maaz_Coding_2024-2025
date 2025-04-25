from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/submitForm", methods=["POST"])
def checkPassword():
    name = request.form("name")
    password = request.form("password")

    if name == "Maaz" and password == "1234":
        return f"<h1>Login Successful. Welcome, {name}.</h1>"
    else:
        return "<h1>Login incorrect. Try again later.</h1>"
    
@app.route("/name/<name>")
def showName(name):
    return f"<h1> Hello, {name}."
    
def main() -> None:
    app.run(debug=True)

if __name__ == "__main__":
    main()