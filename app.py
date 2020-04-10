from urllib.request import urlopen
from flask import Flask, jsonify
import matlab.engine
from PIL import Image
from html_and_url.classifier import get_html_url_score
from screenshot import get_screenshot, string_to_image
from flask_cors import CORS
import cv2
import re 
import os

#nomalize path for use on all machines
logo_saved = os.path.normpath('imgs/boa_logo_wide.png')
logo_saved = os.path.join(os.path.dirname(__file__), logo_saved)

# Steps to install matlab engine for python
# 1) install matlab
# 2) cd to "matlabroot\extern\engines\python
# 3) run python setup.py install

# Start matlab engine for communication with matlab scripts
# matlab_folder = r"C:\Users\brian\Desktop\flask-service\matlab_scripts"
matlab_folder = os.path.join(os.path.dirname(__file__),'matlab_scripts')
matlab_engine = matlab.engine.start_matlab()
matlab_engine.cd(matlab_folder, nargout=0)

# Start flask app
app = Flask(__name__)
cors = CORS(app)

# handle ThreatDetector endpoint
@app.route('/v1/threatdetector/<website>')
def get_score(website):
    # get screenshot of suspect website and convert to numpy array
    screenshot_binary_string = get_screenshot(website)
    ss_array = string_to_image(screenshot_binary_string)    
    # get html score, whois response and google page rank
    html_score, whois_response, rank_checker_response = get_html_score(website)
    registration_date = re.findall(r'Registered On:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    registrar = re.findall(r'Registrar:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    update_date = re.findall(r'Updated On:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    state = re.findall(r'State:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    country = re.findall(r'Country:</div><div class="df-value">([^<]+)</div>', whois_response.text)
    
    # save image for matlab
    cv2.imwrite("imgs/screenshot.png", ss_array)
    # path_for_matlab = os.path.join(os.getcwd(), "imgs\screenshot.png")
    path_for_matlab = os.path.join(os.getcwd(), os.path.normpath("imgs/screenshot.png"))
    # get CV score
    blur_score = get_blur_score(path_for_matlab) # score for blur
    logo_score = get_logo_score(path_for_matlab) # score for logo found
    final_score_dict = {
        "prob_ok":str(html_score[0][0]),
        "prob_phish":str(html_score[0][1]),
        "registrar":registrar,
        "registered_on":registration_date,
        "expiration_date":update_date,
        "state":state,
        "country":country,
        "blurriness": str(blur_score),
        "prob_found_logo": str(logo_score)
    }
    return final_score_dict

# returns the html score
def get_html_score(url):
    return get_html_url_score(url)

# returns the blur score
def get_blur_score(website_path):
    return matlab_engine.getBlurScore(website_path, nargout=1)
    
# returns the logo score
def get_logo_score(website_path):
    return matlab_engine.foundLogo(logo_saved, website_path, nargout=1)

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


