from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({"result": result})

@app.route('/sub', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 - num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
