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

@app.route('/peaky')
def peaky():
    return render_template('peaky.html.jinja')

@app.route('/When')
def When():
    return render_template('When.html.jinja')

@app.route('/Attack')
def Attack():
    return render_template('Attack.html.jinja')

@app.route('/sherlock')
def sherlock():
    return render_template('sherlock.html.jinja')

@app.route('/Note')
def Note():
    return render_template('Note.html.jinja')

@app.route('/matrix')
def matrix():
    return render_template('matrix.html.jinja')

@app.route('/interstellar')
def interstellar():
    return render_template('interstellar.html.jinja')

@app.route('/harry')
def harry():
    return render_template('harry.html.jinja')

@app.route('/dark')
def dark():
    return render_template('darkc.html.jinja')

@app.route('/dune')
def dune():
    return render_template('dune.html.jinja')
    
@app.route('/miles')
def miles():
    return render_template('miles.html.jinja')

@app.route('/avengers')
def avengers():
    return render_template('avengers.html.jinja')

@app.route('/noway')
def noway():
    return render_template('spider.html.jinja')

@app.route('/dragon')
def dragon():
    return render_template('dragonball.html.jinja')

@app.route('/deadly')
def deadly():
    return render_template('deadly.html.jinja')

if __name__ == '__main__':
    app.run(debug=True)
