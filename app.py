from flask import Flask, jsonify
import matlab.engine
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
    engine = matlab.engine.start_matlab()
    engine.cd(matlab_folder, nargout=0)
    response = engine.testmatlab()
    return jsonify(response)
