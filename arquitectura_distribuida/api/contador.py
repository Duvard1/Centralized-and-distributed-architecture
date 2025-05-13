import os
import json

FILE = "/tmp/visitas.json"

def handler(request, response):
    # Leer el archivo de visitas o inicializar
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
    else:
        data = {"visitas": 0}

    # Incrementar contador
    data["visitas"] += 1

    # Guardar nuevo valor
    with open(FILE, "w") as f:
        json.dump(data, f)

    # Devolver como JSON
    return response.json(data)
