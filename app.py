from flask import Flask, jsonify
import matlab.engine

matlab_folder = r"C:\Users\brian\Desktop\capstone research\paypal"

app = Flask(__name__)

@app.route("/helloworld")
def helloworld():
    return jsonify("Hello world")

@app.route("/test_matlab")
def test_matlab():
    engine = matlab.engine.start_matlab()
    engine.cd(matlab_folder, nargout=0)
    response = engine.testmatlab()
    return jsonify(response)
