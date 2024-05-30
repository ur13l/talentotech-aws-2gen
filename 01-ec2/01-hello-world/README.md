# Hello World con Flask

## Descripción

Este ejercicio está enfocado en la creación de una aplicación sencilla utilizando Python con el framework Flask y cómo esta posteriormente puede ser desplegada en una instancia de EC2 configurada en clase.

## Objetivo del ejericio
Crear una aplicación en Flask que sea desplegada dentro de una instancia de EC2 corriendo Ubuntu 22.04

## Instrucciones

1. Crear la instancia de EC2 del tipo **t2.micro** con al menos **8GB** de tamaño en disco duro. Es importante considerar que nuestra instancia debe contar con reglas de seguridad que permitan el acceso público al puerto _5000_.

2. Una vez dentro de la instancia, configurar un entorno de Python para instalar Flask y sus dependencias. Primero se actualizan los paquetes y se instala python-3.12-venv

   ```bash
   sudo apt update
   sudo apt install python3.12-venv
   ```

3. Inmediatamente después, se crea el nuevo entorno

   ```bash
   python3 -m venv ./venv
   ```

4. Una vez creado el entorno, se hace uso de él:

   ```bash
   source ./venv/bin/activate
   ```

5. En la terminal se debería visualizar el nombre del entorno habilitado entre paréntesis:

   ```bash
   (venv) ubuntu@ip-172-31-31-147:~$
   ```

6. Una vez abierto el entorno, es necesario instalar las bibliotecas correspondientes:

   ```bash
   pip3 install Flask
   ```

7. Se crea la carpeta para alojar la aplicación. Esta solo contendrá un archivo llamado _app.py_

   ```bash
   mkdir hello-world
   cd hello-world
   touch app.py
   ```

8. Dentro del archivo _app.py_ colocar el contenido que se encuentra en este repositorio:

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=500)
   ```

9. Por último ejecutamos el comando para correr nuestra aplicación:

   ```bash
   python app.py
   ```

Una vez que la aplicación haya sido lanzada, esta debería ser accesible desde el navegador apuntando a la dirección DNS o a la IP asignada a la instancia de EC2 apuntando al puerto 5000.
