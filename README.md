# Entrega1_Gonella_Sofia
Primera entrega del proyecto de página web programado con Python y utilizando framework django.

## Documentacion
Creacion de projecto django (python -m django startproject nombredelproyecto)
Creacion de app django (python -m django startapp App)
Arrancar el servidor (python manage.py runserver)
Descargo y utilizo la plantilla de bootstrap segun mis necesidades para mi proyecto.
Se realiza herencias padre e hijos renderizando las vistas a la plantilla utilizada.

## Inicio
En esta pagina podemos encontrar un vistazo general del grupo GIITNI

## Estudiantes y Profesores
En estas dos paginas podemos agregar estudiantes y profesores a nuestro db.

## Busqueda 
Aca podemos realizar la busqueda de algun estudiante en particular, usando el nombre del mismo. 

## db.sqlite3
Es nuesta base de datos
Para aplicar cambios en base de datos, es decir, transformar nuestros modelos en la base de datos (python manage.py makemigrations) 
Para que impacten en nuestra base de datos (python manage.py migrate)

### views.py
Encontramos las visatas creadas y modeladas para la navegacion y creacion de formularios.

### urls.py
Aca tenemos la configuracion de las rutas que utilizamos.

### models.py
Aca encontramos el modelado de los datos que se usaron en el proyecto y la base de datos

### forms.py
Aca se encuentran los formularios creados y necesarios para poder cargar datos en nuestra base de datos desde la pagina web.