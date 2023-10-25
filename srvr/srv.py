from flask import Flask, request

import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def start_flask_app():
    # Command to start the Flask app with Gunicorn
    command = [
        'gunicorn',
        'srvr.srv:app',  # Replace 'app' with the name of your Flask app object
        '-b', '0.0.0.0:20023',
    ]

    try:
        # Start the Gunicorn process
        subprocess.Popen(command)
        print("Flask app started with Gunicorn.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def log_http_request():
    if request.method == 'GET':
        # Log GET parameters
        params = request.args
        print(f"Received GET request with parameters: {params}")
    elif request.method == 'POST':
        # Log POST parameters
        params = request.form
        print(f"Received POST request with parameters: {params}")
    
    return "Request logged successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20023)