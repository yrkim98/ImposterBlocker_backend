from urllib.request import urlopen

from flask import Flask, jsonify
import matlab.engine
from PIL import Image
# python

# You might want to install matlab engine for python
# 1) install matlab
# 2) cd to "matlabroot\extern\engines\python
# 3) run python setup.py install


# Start matlab engine for communication with matlab scripts
matlab_folder = r"C:\Users\brian\Desktop\capstone research\paypal"
matlab_engine = matlab.engine.start_matlab()
matlab_engine.cd(matlab_folder, nargout=0)

# Start flask app
app = Flask(__name__)

# Hello world endpoint for testing
@app.route("/helloworld")
def helloworld():
    return jsonify("Hello world")

# test_matlab endpoint for testing communication with matlab
@app.route("/test_matlab")
def test_matlab():
    response = matlab_engine.testmatlab()
    return jsonify(response)


@app.route('/get_score/<website>/<imageURL>')
def get_score():
    # put code for capture site here
    website_screenshot = #get site sc here and load it into matlab

# Converts Pillow.Images into matlab matricies.
# Note: possibly convert code to use URL instead of path for easier use?
def convert_to_matlab_image(image_url):
    # Open image using PIL
    image = Image.open(urlopen(image_url))
    # Convert to matlab data types
    image_matlab = matlab.uint8(list(image.getdata()))
    image_matlab.reshape((image.size[0], image.size[1], 3))
    return image_matlab

@app.route('/get_blur_score')
def get_blur_score(image):





