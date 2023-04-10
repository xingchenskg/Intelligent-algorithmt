from flask import Flask
import time
app=Flask(__name__)
@app.route('/sky')
def index__sky():
    time.sleep(2)
    return 'Hello sky'

@app.route('/bobo')
def index__bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/joy')
def index__joy():
    time.sleep(2)
    return 'Hello joy'

if __name__=='main':
    app.run(threaded=True)