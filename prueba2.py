import requests
import json
from string import Template

# Requerimiento 1: Crear templates HTML
img_template = Template('<img src="$url">')
p_es_template = Template('<p>$pajaro</p>')
p_eng_template = Template('<p>$bird</p>')

html_template = Template(
    """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba 02 - Fundamentos de la programación</title>
</head>
<body>
<h1> Aves de Chile </h1>
$body
</body>
</html>"""
)

# Requerimiento 2: Llamar a la API
def request_get(url):
    return json.loads(requests.get(url).text)
    
url = "https://aves.ninjas.cl/api/birds"
result = request_get (url)

imagenes = []
pajaros = []
bird = []

for i in result:
    imagenes.append(i["images"]["main"])
    pajaros.append(i["name"]["spanish"])
    bird.append(i["name"]["english"])
    
    
# Requerimiento 3: Crear archivo html
contenido_body = ""

for i in range(len(imagenes)):
    contenido_body += img_template.substitute(url=imagenes[i]) + "\n"
    contenido_body += p_es_template.substitute(pajaro=pajaros[i]) + "\n"
    contenido_body += p_eng_template.substitute(bird=bird[i]) + "\n"
    
html_template = html_template.substitute(body=contenido_body)

with open("index.html", "wt", encoding="utf-8") as stream:
    stream.writelines(html_template)