from flask import Flask, send_file
import os

app = Flask(__name__)

VIDEO_DIR = 'videos'

@app.route('/')
def index():
    return "Welcome to the Video Streaming Service"

@app.route('/video/<filename>')
def video(filename):
    return send_file(os.path.join(VIDEO_DIR, filename), mimetype='video/mp4')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
