from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name)

def main() -> None:
    app.run(debug=True)    


if __name__ == "__main__":
    main()