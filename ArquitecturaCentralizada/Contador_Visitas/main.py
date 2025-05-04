from flask import Flask
import os

app = Flask(__name__)
contador_archivo = "contador.txt"

# Inicializa el contador si no existe el archivo
if not os.path.exists(contador_archivo):
    with open(contador_archivo, "w") as f:
        f.write("0")

@app.route("/")
def contador():
    # Leer el contador actual
    with open(contador_archivo, "r") as f:
        visitas = int(f.read())

    # Incrementar el contador
    visitas += 1

    # Guardar el nuevo valor
    with open(contador_archivo, "w") as f:
        f.write(str(visitas))

    # Mostrar el resultado
    return f"<h1>Esta página ha sido visitada {visitas} veces</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
