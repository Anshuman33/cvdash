''' Flask application script for serving the web-app'''
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)



@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon'), 200

@app.route('/')
def index():
    '''
        Homepage renderer.
    '''
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
    
