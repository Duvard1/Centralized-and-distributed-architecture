from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir', methods=['GET'])
def convertir():
    celsius = float(request.args.get('celsius', 0))
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({"fahrenheit": fahrenheit})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
