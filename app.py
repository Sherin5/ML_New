from flask import Flask
from Housing.logger import logging
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    logging.info("We are testing the logging module")
    return "Logging module done"

if __name__ =="__main__":
    app.run(debug=True)