import pickle
import subprocess

from flask import Flask, request, jsonify

app = Flask(__name__)

# load the model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from POST request
    data = request.get_json(force=True)
    result = model.predict(data['feature'])
    return jsonify(result[0].tolist())


@app.route('/github_webhook', methods=['POST'])
def rebuild():
    print('new commits to github repository')
    # subprocess.run can just deal with the first change
    # since it stuck in it, use Popen instead
    # subprocess.run(['sh', 'build_and_run.sh'])
    subprocess.Popen(['sh', 'build_and_run.sh'])
    return jsonify('got it')


if __name__ == '__main__':
    app.run(debug=True)
