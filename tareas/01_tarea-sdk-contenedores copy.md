# Integración de funcionalidad adicional a aplicación de Flask

## Descripción del ejercicio

Tomando como referencia la aplicación desarrollada durante el ejercicio 2 y el ejercicio 3, implementar funcionalidad adicional para mostrar información acerca de la unidad de disco duro vinculada a cada instancia, así como su grupo de seguridad.

## Objetivo del ejericio
El objetivo principal es agregar dos secciones a la pantalla mostrada en la ruta **/instance/\<id\>**, donde actualmente se puede visualizar el rendimiento de CPU de cada instancia. Las dos secciones consisten en lo siguiente:

1. **Sección de volúmenes:** Deberá listar cada uno de los volúmenes de disco duro del servicio EBS añadidos a la instancia de servidor seleccionada. En esta sección se deben mostrar al menos los siguientes datos por cada volumen:

   - ID del volumen.
   - Fecha de creación.
   - Estado
   - Tamaño (en GB)

2. **Sección de Grupos de segudirad::** Esta sección debe mostrar las reglas de entrada y de salida de, al menos, un grupo de seguridad, para cada regla se deberá mostrar lo siguiente:

   - Si es regla de ingreso o egreso.
   - El protocolo IP.
   - El rango de puertos.
   - Bloque de direcciones IP permitidos.

Una vez aplicados los nuevos cambios, se generará un archivo zip con todo el contenido de la carpeta (excepto la carpeta **.venv**). Para validar los cambios se pueden utilizar los comandos `docker build` y `docker run` explicados en la práctica 3.

## Consideraciones

- Para completar esta práctica será necesario modificar los permisos del usuario de AWS CLI para que pueda obtener información sobre los los volúmenes de EBS, grupos de seguridad y reglas de los grupos de seguridad. Revisar [Lista de permisos disponibles de EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html).

- La práctica debe estar desarrollada utilizando el SDK de AWS (boto3) y puede utilizar cualquier elemento disponible en la documentación, ya sea en forma de recurso o cliente de la biblioteca.
  [Revisar documentación](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html).

- La práctica se considerará completa siempre y cuando se entregue el código fuente para la generación de una imagen de Docker en formato de archivo comprimido, no es obligatorio poner en marcha la imagen en algún servicio de la plataforma. Para profundizar más en el tema, revisar la sección de **Retos adicionales**.

## Instrucciones de entrega

1. Una vez realizadas las modificaciones a la app, el proyecto debe contar con un archivo Dockerfile que permita la carga de una clave de acceso de AWS como parámetro para su construcción.

2. La práctica debe subirse a la plataforma en formato zip (comprimir la carpeta del proyecto).

## Retos adicionales (opcionales)

- Publicar la imagen de contenedor en el repositorio de ECR con la etiqueta _latest_.
- Actualizar la ejecución del servicio y tarea de ECS desplegados en la sesión.
- Crear la misma aplicación utilizando otro lenguaje de programación como Java, Javascript, PHP, etc.
