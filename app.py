from flask import Flask, render_template
from notebook import notebookapp
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Start notebook server
    nb_app = notebookapp.NotebookApp.instance()
    nb_app.initialize([])
    nb_app.start()

    # Get notebook URL
    notebook_url = nb_app.connection_url
    return render_template('index.html', notebook_url=notebook_url)

if __name__ == '__main__':
    app.run(debug=True)
