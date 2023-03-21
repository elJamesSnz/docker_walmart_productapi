# docker_walmart_productapi
 
# 1. Librerías usadas

## Lista de las librerías utilizadas en el proyecto.
- Selenium
- DJangorestframework
- webdriver-manager

Lista de frameworks utilizados.
- DJango

# 2. Pasos para instalación
Instrucciones para instalar proyecto (VS Code)

## Clonar proyecto
Usar Github Desktop

## Iniciar contenedor docker
docker build -t django_project .

## Ejecutar contenedor
docker run -d -p 8080:8000 django_project

# 3. Posibles incidencias
Lista de posibles incidencias.

## 3.1 Bloqueos
Walmart no es amigable para desarrolladores que intentan obtener información de su página a través de web scraping. Tienen desafíos que buscan prevenir el uso de bots / webdrivers

## 3.2 Complejidades
La terminal de VS Code no encuentra un intérpte de Python y/o ambiente de desarrollo correcto
CTRL + SHIFT + P -> Seleccionar intérprete -> seleccionar recomendado (./venv/)
Para el segundo ejercicio, desde la página a la que se accede en Walmart (listado de productos por categoría seleccionada) se presenta un bloqueo adicional que no permite recuperar los productos desde el contenedor

## 3.3 Retrasos
El aplicativo puede tardar en recuperar la información (valida si hay desafío anti bot que consiste en hacer click en la página y hacer hold de ese click por cierta cantidad de segundos).
Se puede ver en consola el mensaje "Click & hold verificado" cuando tuvo que cumplir con el desafío
Se puede ver en consola el mensaje "no hay click and hold" cuando no tuvo que cumplir con el desafío


# 4 Uso
Instrucciones para su uso.

## 4.1 PRIMER EJERCICIO. (walmartscraperapi)
### Iniciar contenedor docker
docker build -t django_project .
### Ejecutar contenedor
docker run -d -p 8080:8000 django_project

NOTA: 8080 es el puerto local que se comparte con el puerto 8000 del contenedor. Si se cambia el 8080 por otro puerto, la URL debe tener el nuevo puerto asignado.

e.g. docker run -d -p 8070:8000 django_project -> http://127.0.0.1:8070/api/scraper/despensa/

### 4.1.2 Obtener JSON (POSTMAN o Cliente REST)

En Postman o Cliente REST hacer request GET
URL. http://127.0.0.1:8080/api/scraper/despensa/

![image](https://user-images.githubusercontent.com/72090281/226526745-9154f523-5206-45d8-9d69-0f3242a44f37.png)

Salida

![image](https://user-images.githubusercontent.com/72090281/226526789-20ffd742-dd03-4145-9b8a-530da950cc87.png)

### 4.1.2 Obtener JSON (Navegador)
Ingresar URL http://127.0.0.1:8080/api/scraper/despensa/

NOTA. Para ambos casos, la petición tarda por la posible verificación click & hold.

## 4.2 SEGUNDO EJERCICIO. (docker_walmart_productapi)

### 4.2.1 Obtener JSON (POSTMAN o Cliente REST)

En Postman o Cliente REST hacer request GET
URL. http://127.0.0.1:8080/api/scraper/categoria/
Agregar url a los parámetros del BODY. RAW -> JSON 

{    
    "url": "https://super.walmart.com.mx/content/abarrotes/cafe-te-y-sustitutos/120005_120070"
}

![image](https://user-images.githubusercontent.com/72090281/226527257-a55dc715-8b80-446a-9965-0308dddbf0e1.png)


Nota: El URL debe ser alguna subcategoría del URL https://super.walmart.com.mx/all-departments

Salida.

Para el segundo ejercicio, desde la página a la que se accede en Walmart (listado de productos por categoría seleccionada) se presenta un bloqueo adicional que no permite recuperar los productos desde el contenedor de Docker

![image](https://user-images.githubusercontent.com/72090281/226670580-f3541e05-9a51-43a9-b965-d40be9bc1da0.png)

La salida esperada se encuentra en el repo de ejecutables: https://github.com/elJamesSnz/walmart-webscraping-apps

![image](https://user-images.githubusercontent.com/72090281/226673475-95d69889-861f-4887-b3d3-c69376f3d0fa.png)

# Autor
Angel Sánchez

