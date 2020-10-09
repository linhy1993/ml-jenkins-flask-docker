from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# test
@app.route('/github_webhook', methods=['POST'])
def rebuild():
    print('new commits to github repository')
    # subprocess.run can just deal with the first change
    # since it stuck in it, use Popen instead
    # subprocess.run(['sh', 'build_and_run.sh'])
    subprocess.Popen(['sh', 'build_and_run.sh'])
    return jsonify('got it')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
