from flask import Flask,request
from subprocess import check_output

app = Flask(__name__)

@app.route("/deploy", methods=['POST'])
def deploy():
    shPath = request.json.get('executePath')
    out = check_output([shPath, "-p"])

    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)