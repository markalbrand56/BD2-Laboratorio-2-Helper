import requests
import random
import time

"""
Generación random de usuarios
Campos: 
- nombre (string)
- email (string)
- fecha_registro (date)
- puntos (int)
- historial_compras [array conformado por documentos embebidos con datos de productos (string) y fecha (date)]. 
    Al generar estos datos asegúrese de generar suficiente información del producto llamado "Producto 1". Le servirá más adelante.
- dirección [documento embebido con datos de calle (string), ciudad (string), codigo_postal (int)]
- tags (array de strings). Al momento de generar estos valores, asegúrese de incluir suficientes valores con la 
    etiqueta "tag2". El resto podrá quedar a su discreción.
- archivo (boolean)
- notas (string)
- visitas (entero)
- amigos (arrays de enteros). Genere algunos usuarios que tengan más de mil amigos
- preferencias [documento embebido con datos de color (string), idioma (string) y tema (string)]
"""


def get_random_user():
    data = requests.get("https://random-data-api.com/api/v2/users")
    data = data.json()

    tags = []
    for i in range(random.randint(1, 10)):
        tags.append(f"tag{random.randint(1, 10)}")

    amigos = []
    for i in range(random.randint(0, 5000)):
        id = random.randint(1, 999999)

        while id in amigos:
            id = random.randint(1, 999999)

        amigos.append(id)

    historial_compras = []
    for i in range(random.randint(0, 10)):
        random_date_offset = random.randint(0, 120)  # 0 a 120 días atrás
        random_date = time.strftime("%Y-%m-%d", time.localtime(time.time() - random_date_offset * 24 * 60 * 60))

        historial_compras.append({
            "producto": random.choice(["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]),
            "fecha": random_date
        })

    user = {
        "nombre": f"{data['first_name']} {data['last_name']}",
        "email": data["email"],
        "fecha_registro": data["date_of_birth"],
        "puntos": random.randint(0, 5000),
        "historial_compras": historial_compras,
        "direccion": {
            "calle": data["address"]["street_address"],
            "ciudad": data["address"]["city"],
            "codigo_postal": data["address"]["zip_code"]
        },
        "tags": tags,
        "archivo": random.choice([True, False]),
        "notas": f"{data['employment']['title']}: {data['employment']['key_skill']}",
        "visitas": random.randint(0, 10000),
        "amigos": amigos,
        "preferencias": {
            "color": random.choice(["red", "blue", "green", "yellow", "black", "white"]),
            "idioma": random.choice(["es", "en", "fr", "de", "it"]),
            "tema": random.choice(["light", "dark"])
        }
    }

    return user


if __name__ == "__main__":
    for i in range(5):
        u = get_random_user()
        for k, v in u.items():
            print(f"{k}: {v}")
        print()
