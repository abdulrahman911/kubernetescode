from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello There, Please like my DevOps projects, By Abdul Rahman UK Thank you!!!'
