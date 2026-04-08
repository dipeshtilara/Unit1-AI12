from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Return the HTML file directly
    return send_file('data_science_methodology.html')

if __name__ == '__main__':
    # Use the PORT environment variable if available (e.g., for Render/Heroku), otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
