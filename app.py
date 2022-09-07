from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello There, Please subscribe, like, and comment on this video, By Abdul Rahman UK Thank you!!!'
