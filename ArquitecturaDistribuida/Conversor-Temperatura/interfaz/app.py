from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def inicio():
    return '''
        <h2>Conversor de Temperatura</h2>
        <form action="/convertir" method="get">
            Celsius: <input name="celsius" type="number" step="any"/>
            <button type="submit">Convertir</button>
        </form>
    '''

@app.route('/convertir')
def convertir():
    celsius = request.args.get('celsius', 0)

    f = requests.get(f'http://fahrenheit:5001/convertir?celsius={celsius}').json()
    k = requests.get(f'http://kelvin:5002/convertir?celsius={celsius}').json()

    return f"""
        <h2>Resultado para {celsius}°C</h2>
        <p>Fahrenheit: {f['fahrenheit']}°F</p>
        <p>Kelvin: {k['kelvin']}K</p>
        <a href="/">Volver</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
