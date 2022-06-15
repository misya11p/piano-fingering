from flask import Flask, render_template
import sys; sys.path.insert(0, './modules')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()