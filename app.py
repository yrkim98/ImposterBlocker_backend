from urllib.request import urlopen

from flask import Flask, jsonify
import matlab.engine
from PIL import Image
from html_and_url.classifier import get_html_url_score
from screenshot import get_screenshot, string_to_image

# You might want to install matlab engine for python
# 1) install matlab
# 2) cd to "matlabroot\extern\engines\python
# 3) run python setup.py install


# # Start matlab engine for communication with matlab scripts
# matlab_folder = r"C:\Users\brian\Desktop\capstone research\paypal"
# matlab_engine = matlab.engine.start_matlab()
# matlab_engine.cd(matlab_folder, nargout=0)

# Start flask app
app = Flask(__name__)

# Hello world endpoint for testing
@app.route("/helloworld")
def helloworld():
    return jsonify("Hello world")

# test_matlab endpoint for testing communication with matlab
# @app.route("/test_matlab")
# def test_matlab():
#     response = matlab_engine.testmatlab()
#     return jsonify(response)


@app.route('/get_score/<website>')
def get_score(website):
    # put code for capture site here
    # website_screenshot = #get site sc here and load it into matlab

    ss = get_screenshot(website)
    ss_array = string_to_image(ss)
    html_score = get_html_score(website)
    # image_score = get_image_score()
    html_score_dict = {
        "prob_ok":str(html_score[0][0]),
        "prob_phish":str(html_score[0][1])
    }
    print(ss_array)

    return html_score_dict


def get_html_score(url):
    return get_html_url_score(url)

# Converts Numpy arrays into matlab matricies.
# Note: possibly convert code to use URL instead of path for easier use?
def convert_to_matlab_image(image_numpy):
    # Open image using PIL
    image = Image.fromarray(image_numpy.astype('uint8'), 'RGB')
    # Convert to matlab data types
    image_matlab = matlab.uint8(list(image.getdata()))
    image_matlab.reshape((image.size[0], image.size[1], 3))
    return image_matlab



# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()


