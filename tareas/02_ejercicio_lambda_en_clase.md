# Creación de una API REST con AWS API Gateway y AWS Lambda

## Descripción del ejercicio

De acuerdo a lo visto en las sesiones anteriores, durante este ejercicio se propone la creación de una API REST que sea accesible desde Internet de forma pública y ejecute alguna de las acciones descritas en el **Objetivo del ejercicio**.

## Objetivo del ejericio
Utilizando AWS API Gateway y AWS Lambda, crear una API REST con endpoints para realizar diferentes funcionalidades. Cada equipo podrá elegir la lógica del (o los) endpoint(s) que quiera implementar, basados en la siguiente lista:

1. **Calculadora API:**
   **Objetivo**: Implementar una API que realice operaciones básicas (suma, resta, multiplicación, división).

   ***

2. **API de Conversión de Monedas**:
   **Objetivo**: Crear una API que convierta una cantidad de una moneda a otra utilizando un tipo de cambio estático.

   ***

3. **API para Procesamiento de Textos**:
   **Objetivo**: Desarrollar una API que pueda contar palabras, caracteres y párrafos en un texto dado.

## Consideraciones

- Independientemente de la API elegida, este

## Instrucciones de entrega

1. Una vez realizadas las modificaciones a la app, el proyecto debe contar con un archivo Dockerfile que permita la carga de una clave de acceso de AWS como parámetro para su construcción.

2. La práctica debe subirse a la plataforma en formato zip (comprimir la carpeta del proyecto).

## Retos adicionales (opcionales)

- Crear la misma aplicación utilizando otro lenguaje de programación como Java, Javascript, PHP, etc.
- Publicar la imagen de contenedor en ECR y ponerlo en marcha utilizando Elastic Container Service (ECS). **Puede generar costos adicionales en AWS**.
