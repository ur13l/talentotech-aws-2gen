# Creación de un contenedor de aplicación

## Descripción

En este ejercicio, se tomará como referencia el ejercicio desarrollado en la [práctica 2](https://github.com/ur13l/talentotech-aws-2gen/tree/main/02-sdk/02-aws-sdk-app) y se le añadirán funcionalidades para desplegarlo como un contenedor de Docker.

## Objetivo del ejericio
El objetivo del ejercicio es la preparación de una aplicación web en Python y sus paquetes para su despliegue en el servicio de Amazon Elastic Container Service (ECS) y su acceso a nivel general.

## Requisitos previos

- Contar con el proyecto de la práctica 2 funcional.
- Tener una clave de acceso para la cuenta de AWS con permisos de lectura de EC2 y CloudWatch.
- Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/).

## Instrucciones

1. Crear una copia de la práctica 2, incluyendo todos sus archivos (_app.py_ y la carpeta _templates_).

2. Crear un archivo de dependencias llamado **requirements.txt**, este incluirá las bibliotecas necesarias para ejecutar nuestra aplicación:

   ```python
   Flask===3.0.3
   boto3===1.34.121
   gunicorn===22.0.0
   ```

3. Crear un archivo llamado _Dockerfile_ con el siguiente contenido:

   ```docker
    # Usa una imagen base oficial de Python con la plataforma de linux/amd64 (misma que utilizan las instancias de EC2)
    FROM --platform=linux/amd64 python:3.10-slim

    # Establece un directorio de trabajo (Dentro del sistema de archivos del contenedor)
    WORKDIR /app

    # Copia los archivos de requisitos primero para aprovechar la caché de Docker
    COPY requirements.txt /app/
    RUN pip install -r requirements.txt

    # Recibe la llave y el secret access key como parámetros de compilación
    ARG AWS_ACCESS_KEY_ID
    ARG AWS_SECRET_ACCESS_KEY

    # Asignar las variables de entorno con los valores que vienen de los parámetros
    ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
    ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

    # Copia el resto de tu código de aplicación
    COPY . /app

    # Indica el puerto que va a exponer el contenedor
    EXPOSE 5000

    # Define el comando para ejecutar tu aplicación usando Gunicorn
    CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
   ```

4. Una vez creada la configuración del Dockerfile, la aplicación deberá poder compilarse utilizando el siguiente comando:

   ```bash
   docker build -t ec2-app . --build-arg AWS_ACCESS_KEY_ID=XXXXXXX --build-arg AWS_SECRET_ACCESS_KEY=XXXXXX
   ```

   **NOTA:** Asegúrate de reemplazar los valores de AWS_ACCESS_KEY_ID y de AWS_SECRET_ACCESS_KEY en la ejecución del comando.

5. Para corroborar que todo funciona correctamente, con el siguiente comando puedes ejecutar el contenedor:

   ```bash
   docker run -p 5000:5000 ec2-app
   ```

6. Una vez asegurado que se ejecuta el contenedor, se debe realizar el proceso de cargado en ECR, para esto es necesario crear un nuevo repositorio privado en la consola de AWS dentro del servicio de ECR.

7. Creado el repositorio, se necesitan ejecutar los siguientes comandos, el primero es para vincular nuestra cuenta de AWS con el comando de Docker, lo que permitirá publicar nuestra imagen en el servicio de registros:

   ```bash
   aws ecr get-login-password --region us-east-1 --profile admin | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
   ```

   **NOTA 1:** La instrucción `--profile admin` indica que debes contar con una clave de acceso configurada en tu equipo local con permisos para publicar imágenes en ECR. En clase se mostrará este proceso para dar de alta una clave del usuario administrador. La modificación realizada corresponde a modificar el archivo `~/.aws/credentials`(Linux/MacOS) o `C:\Users\USERNAME\.aws\credentials`(Windows) y agregar lo siguiente

   ```bash
   [admin]
   aws_access_key_id=<XXXXXXXXX>
   aws_secret_access_key=<XXXXXXXXXXXXXXXXXXXXXX>
   ```

   Asímismo, también se añade lo siguiente al archivo `~/.aws/config`(Linux/MacOS) p `C:\Users\USERNAME\aws\config`(Windows).

   ```bash
   [admin]
   region=us-east-1
   output=json
   ```

   **NOTA 2:** Asegúrate de reemplazar **<AWS_ACCOUNT_ID>** la URL del registro, este debe ser tu propio ID de cuenta de AWS.

8. Después de haberle dado permisos a nuestra configuración de Docker, ahora es posible publicar la primera versión de la imagen que contiene nuestra aplicación:

   ```bash
   docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ec2-app:latest
   ```
