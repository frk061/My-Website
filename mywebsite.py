from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('aufbau.html.jinja')

@app.route('/aufbau')
def other_page():
    return render_template('aufbau2.html.jinja')

@app.route('/goback')
def go_back():
    return render_template('aufbau.html.jinja')
    
if __name__ == '__main__':
    app.run(debug=True)