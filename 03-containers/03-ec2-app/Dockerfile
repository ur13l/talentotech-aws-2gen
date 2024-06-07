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

# Ejemplo de cómo correr con las variables de entorno y argumentos en compilación
# docker build --build-arg AWS_KEY_ID=XXXXXXX --build-arg AWS_SECRET_ACCESS_KEY=XXXXXXX -t ec2-app .