from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<name>')
def index(name):
    naam = "<strong>Anukul</strong>"
    return render_template('user.html', user_name = name , naam = naam)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html') ,404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html') ,500

if __name__ == "__main__":
    app.run(debug=True)