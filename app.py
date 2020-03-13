from urllib.request import urlopen
from flask import Flask, jsonify
# import matlab.engine
from PIL import Image
from html_and_url.classifier import get_html_url_score
from screenshot import get_screenshot, string_to_image
from flask_cors import CORS
import cv2
import re 
import os

logo_saved = r'C:\Users\brian\Desktop\capstone research\paypal\boa_logo_wide.png'


# You might want to install matlab engine for python
# 1) install matlab
# 2) cd to "matlabroot\extern\engines\python
# 3) run python setup.py install


# # Start matlab engine for communication with matlab scripts
# matlab_folder = r"C:\Users\brian\Desktop\flask-service\matlab_scripts"
# matlab_engine = matlab.engine.start_matlab()
# matlab_engine.cd(matlab_folder, nargout=0)

# Start flask app
app = Flask(__name__)
cors = CORS(app)

# Hello world endpoint for testing
@app.route("/helloworld")
def helloworld():
    return jsonify("Hello world")

# def get_blur_score(website_path):
#     return matlab_engine.getBlurScore(website_path, nargout=1)

def get_found_score(website_path):
    return matlab_engine.foundLogo(logo_saved, website_path, nargout=1)

@app.route('/get_score/<website>')
def get_score(website):
    # put code for capture site here
    # website_screenshot = #get site sc here and load it into matlab

    ss = get_screenshot(website)
    ss_array = string_to_image(ss)
    html_score, whois_response, rank_checker_response = get_html_score(website)
    registration_date = re.findall(r'Registered On:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    registrar = re.findall(r'Registrar:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    update_date = re.findall(r'Updated On:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    state = re.findall(r'State:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    country = re.findall(r'Country:</div><div class="df-value">([^<]+)</div>', whois_response.text)

    # save image for matlab
    cv2.imwrite("imgs/screenshot.png", ss_array)
    path_for_matlab = os.path.join(os.getcwd(), "imgs\screenshot.png")
    blur_score = get_blur_score(path_for_matlab) # score for blur
    found_score = get_found_score(path_for_matlab) # score for found logo

    final_score_dict = {
        "prob_ok":str(html_score[0][0]),
        "prob_phish":str(html_score[0][1]),
        "registrar":registrar,
        "registered_on":registration_date,
        "expiration_date":update_date,
        "state":state,
        "country":country,
        "blurriness": str(blur_score),
        "prob_found_logo": str(found_score)
    }

    return final_score_dict



def get_html_score(url):
    return get_html_url_score(url)

# Converts Numpy arrays into matlab matricies.
# Note: possibly convert code to use URL instead of path for easier use?
def convert_to_matlab_image(image_numpy):
    # Open image using PIL
    image = Image.fromarray(np.uint8(image_numpy))
    # # Convert to matlab data types
    # image_matlab = matlab.uint8(list(image.getdata()))
    # image_matlab.reshape((image.size[0], image.size[1], 3))
    return image










# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run()


