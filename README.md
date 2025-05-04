# 🧠 Proyecto: Comparación entre Arquitectura Centralizada y Distribuida
Este repositorio presenta dos implementaciones funcionales que demuestran la diferencia entre una arquitectura centralizada y una arquitectura distribuida, utilizando Python (Flask) y Docker como herramientas principales.
Ambos ejemplos están pensados para ejecutarse localmente y ser publicados en DockerHub.

## 🔹 Parte 1: Arquitectura Centralizada – Contador de Visitas
Una aplicación web monolítica que muestra cuántas veces se ha accedido a la página. El contador se almacena localmente en un archivo y todo ocurre en un solo servicio.

📁 Carpeta: ArquitecturaCentralizada/Contador_Visitas

## 🔸 Parte 2: Arquitectura Distribuida – Conversor de Temperatura
Una aplicación dividida en microservicios que convierte grados Celsius a Fahrenheit y Kelvin.
Cada servicio está desacoplado y cumple una tarea específica.

📁 Carpeta: ArquitecturaDistribuida/Conversor-Temperatura

### 🔧 Servicios:

interfaz (UI)

fahrenheit (microservicio)

kelvin (microservicio)


### 🐳 Imágenes Docker: 
duvard/interfaz

duvard/fahrenheit

duvard/kelvin


### 🧰 Tecnologías usadas
Python + Flask

Docker & DockerHub

Docker Compose

GitHub

## 🚀 Ejecución de los Proyectos
### 1️⃣ Arquitectura Centralizada – Contador de Visitas

Construye la imagen Docker:
docker build -t duvard/contador-visitas:v1 .

Ejecuta el contenedor:
docker run -p 5000:5000 tu_usuario/contador-visitas:v1

Accede a la aplicación:
👉 http://localhost:5000

### 2️⃣ Arquitectura Distribuida – Conversor de Temperatura

Construye y ejecuta los microservicios con Docker Compose:
docker-compose up --build

Accede a la aplicación:
👉 http://localhost:5000




### 📌 Autor
Este proyecto fue desarrollado con fines educativos para demostrar los principios de arquitecturas centralizadas y distribuidas, usando microservicios y contenedores.

### 📂 Estructura del repositorio
![image](https://github.com/user-attachments/assets/2142977a-6948-44a0-9e17-6fc8e45b38ed)
