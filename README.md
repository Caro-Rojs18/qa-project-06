

# Qa-project-06

E**ste proyecto busca iniciar la automatizacion para sustituir el proceso manual que se han estado utilizando los sprint 
anteriores.
En este sprint, se practica  la automatización de los casos de prueba con el lenguaje de programación Python.


## **por que es importante?**

⏳ La automatización acelera las pruebas. A veces, el proceso de prueba se puede reducir de una semana a una hora. 

⚙️ Hay menos rutina. Puedes liberar tiempo para hacer tareas más interesantes o estudiar nuevas tecnologías.

⛔️ Se reduce el riesgo de error. Los programas informáticos no se cansan ni se distraen.

🤖 La programación se realiza en entornos de desarrollo integrados que admiten el lenguaje de programación requerido. Un ejemplo de un IDE es PyCharm.

🐞 Los y las testers pueden automatizar las pruebas de regresión con Python, JavaScript o algún otro lenguaje de programación.

🔥 Para llevar la aplicación a producción, primero debes configurar las herramientas para el ensamblaje y el despliegue. Esto se puede hacer con herramientas como Jenkins.

##### En este protecto conociendo  La interfaz de PyCharm, y para realizar los testcase Pytest en PyCharm, Pytest  reconoce las pruebas basándose en un prefijo específico. Las funciones que comienzan con test (en minúsculas) son tratadas como pruebas.

# **_PROPOSITO_**

Urban Grocers para  el espacio **name** en la #solicitud de creacion de un kit de productos!

### Acerca del proyecto 

Para iniciar se debe conocer la documentacion para iniciar el ejercicio de automatizacio de la lista de comprobacion 

Urban Grocers Documentation API: https://cnt-2cb651cb-2d3a-42a8-bafd-281348aa0aa2.containerhub.tripleten-services.com/docs/

  
![Image (3).png](..%2F..%2F..%2FDownloads%2FImage%20%283%29.png)





## Se inicia 
### La librería de solicitudes de Python: solicitudes POST

Desde Python Packages se puede acceder a las funciones de la libreria requests que nos permitirá gestionar las solicitudes HTTP de manera sencilla.

la intencion es realizar una solicitud de HTTP usando Python Puedes enviar una solicitud mediante la librería requests de Python. Solo necesitas llamar a la

función get() y proporcionarle la URL completa a la que deseas acceder.

el proyecto esta organizado con-------Configuración de la ruta
                                      Datos de la solicitud
                                      Importación de datos
                                      Envío de la solicitud POST

vamos con la solicitud POST para crear un kit iniciando con el usuario 

(CREATE_USER_PATH, KITS_PATH) 


### Principios Fundamentales


Para que tus pruebas automatizadas sean efectivas y fáciles de mantener, es crucial seguir ciertos principios:

Unidad de comprobación. Cada prueba debe centrarse en una única funcionalidad o aspecto. Esto facilita la identificación de problemas y la corrección de errores.

Independencia de datos. Evita depender de datos específicos que puedan cambiar con el tiempo. En su lugar, genera o utiliza datos que sean consistentes para la prueba.

Autonomía de las pruebas. Cada prueba debe ser capaz de ejecutarse de forma independiente, sin depender del resultado de otras pruebas.

De esta  manera le damos lugar a la creacion de **Autotest**

### Tenemos TEST en este proyecto como

Positive_assert comprueba si el código de estado (status_code) de la respuesta es igual al código de estado esperado y si el nombre (name) devuelto en la respuesta coincide con el nombre esperado.

Negative_assert comprueba si el código de estado (status_code) de la respuesta es igual al código de estado esperado, sin realizar comprobaciones adicionales sobre el cuerpo de la respuesta.**

Archivos especiales de proyectos: gitignore y README