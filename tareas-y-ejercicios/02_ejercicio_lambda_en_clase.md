# Creación de una API REST con AWS API Gateway y AWS Lambda

## Descripción del ejercicio

De acuerdo a lo visto en las sesiones anteriores, durante este ejercicio se propone la creación de una API REST que sea accesible desde Internet de forma pública y ejecute alguna de las acciones descritas en el **Objetivo del ejercicio**.

## Objetivo del ejericio

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

- De las opciones disponibles, solo se debe elegir una.
- Considerar el mecanismo para pasar la información, se puede utilizar el método GET o POST y pasar la información por queryStrings o el cuerpo(body) de la petición.

## Instrucciones de entrega

1. La práctica debe crearse utilizando SAM y publicarse con sam deploy.
2. Se debe compartir el enlace del endpoint ge
