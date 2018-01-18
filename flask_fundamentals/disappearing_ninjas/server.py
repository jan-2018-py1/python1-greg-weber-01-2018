from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def img_picker(color):
    if (color == 'blue' or color == 'orange' or color == 'red' or color == 'purple'):
        return render_template('ninja'+ color +'.html')
    else:
        return render_template('not_a_ninja.html')

app.run(debug = True)