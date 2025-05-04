from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir', methods=['GET'])
def convertir():
    celsius = float(request.args.get('celsius', 0))
    kelvin = celsius + 273.15
    return jsonify({"kelvin": kelvin})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)