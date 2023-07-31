from flask import Flask
from Housing.exception import HousingException
import sys
from Housing.logger import logging
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    try:
        raise Exception("Testing the custom exception class")
    except Exception as e:
        housing_error = HousingException(e, sys)
        logging.info(housing_error.error_message)
        logging.info("We are testing the logging module")
    return "Exception module done"

if __name__ =="__main__":
    app.run(debug=False)