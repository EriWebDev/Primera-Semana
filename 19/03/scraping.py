import requests
from bs4 import BeautifulSoup   #importar biblioteca BeautifulSoup
from requests import get    #importar función get()
#indicar la URL para descargar el HTML en una lista
countries = {
    "Grecia": "https://es.wikipedia.org/wiki/Grecia",
    "Italia": "https://es.wikipedia.org/wiki/Italia"
}

#hay que recorrer la lista para cada país, con un bucle for
for country, url in countries.items():
    #print para mostrar por consola la información
    print("Información sobre", country)

#petición para obtener el HTML
petition = requests.get(url)

#almacenamos la respuesta del servidor en una variable
if petition.status_code == 200: #200 si se encuentra
    html = petition.text
else:
    print("Error", petition.status_code) #error si se tiene problemas al acceder a la página

#creamos un objeto para "almacenar" el HTML
soup = BeautifulSoup(html, "html.parser")

#empezamos a sacar la información
history = soup.find("h2", {"id": "Historia"}) #buscamos el título para la historia
