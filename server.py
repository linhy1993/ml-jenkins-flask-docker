import pickle
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)

# load the model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from POST request
    data = request.get_json(force=True)
    result = model.predict(data['feature'])
    return jsonify(result[0].tolist())


if __name__ == '__main__':
    app.run(debug=True)
