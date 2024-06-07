# Integración de funcionalidad adicional a aplicación de Flask

## Descripción del ejercicio

Tomando como referencia la aplicación desarrollada durante el ejercicio 2 y el ejercicio 3, implementar funcionalidad adicional para mostrar información acerca de la unidad de disco duro vinculada a cada instancia, así como su grupo de seguridad.

## Objetivo del ejericio
El objetivo principal es agregar dos secciones a la pantalla mostrada en la ruta **/instance/\<id\>**, donde actualmente se puede visualizar el rendimiento de CPU de cada instancia. Las dos secciones consisten en lo siguiente:

1. **Sección de volúmenes:** Deberá listar cada uno de los volúmenes de disco duro del servicio EBS añadidos a la instancia de servidor seleccionada. En esta sección se deben mostrar al menos los siguientes datos por cada volumen:

   a. ID del volumen.
   b. Fecha de creación.
   c. Estado
   d. Tamaño (en GB)

2. **Sección de Grupos de segudirad::** Esta sección debe mostrar las reglas de entrada y de salida de, al menos, un grupo de seguridad, para cada regla se deberá mostrar lo siguiente:

   a. Si es regla de ingreso o egreso.
   b. El protocolo IP.
   c. El rango de puertos.
   d. Bloque de direcciones IP permitidos.

## Consideraciones

- Para completar esta práctica será necesario modificar los permisos del usuario de AWS CLI para que pueda obtener información sobre los los volúmenes de EBS, grupos de seguridad y reglas de los grupos de seguridad. Revisar [Lista de permisos disponibles de EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html).

- La práctica debe estar desarrollada utilizando el SDK de AWS (boto3) y puede utilizar cualquier elemento disponible en la documentación, ya sea en forma de recurso o cliente de la biblioteca.
  [Revisar documentación](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html).

## Instrucciones de entrega

1. Una vez realizadas las modificaciones a la app, el proyecto debe contar con un archivo Dockerfile que permita la carga de una clave de acceso de AWS como parámetro para su construcción.

2. La práctica debe subirse a la plataforma en formato zip (comprimir la carpeta del proyecto).

## Retos adicionales (opcionales)

- Crear la misma aplicación utilizando otro lenguaje de programación como Java, Javascript, PHP, etc.
- Publicar la imagen de contenedor en ECR y ponerlo en marcha utilizando Elastic Container Service (ECS). **Puede generar costos adicionales en AWS**.
