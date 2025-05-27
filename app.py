# app.py
import os
from flask import Flask, render_template

app = Flask(__name__)

# User provided Google Maps API Key
GOOGLE_MAPS_API_KEY = "AIzaSyAHN4UMtZRhSGTX7dBQAES7ISB6L3ozVC0"

@app.route('/')
def main_app():
    """
    Serves the single-page application.
    All HTML, CSS, and JS will be in 'app_shell.html'.
    """
    return render_template('app_shell.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

if __name__ == '__main__':
    app.run(debug=True, port=5001)