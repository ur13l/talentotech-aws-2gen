FROM amazon/aws-lambda-python:3.10

LABEL maintainer="Uriel Infante"

# # Instalar python y las dependencias necesarias para ejecutar psycopg2
# RUN yum update -y && \
#     yum install -y python3 python3-dev python3-pip gcc postgresql-devel && \
#     rm -Rf /var/cache/yum

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt ./

# Instalación de dependencias basadas en el archivo requirements.txt
RUN pip install -r requirements.txt

# Se copia, por último, el código de la función lambda.
COPY metadata_function.py ./

# Se apunta al handler de la función para su ejecución.
CMD ["metadata_function.handler"]