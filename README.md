# Blog Django
Projecto Django inicial de un blog
## Descripcion
Repositorio inicial de un blog usando Django
## Instalacion
Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto

```
cd NOMBRE_DEL_REPOSITORIO
```

Crear entorno virtual

```
python -m venv venv
```

Activar entorno virtual:
En windows PowerShell:
```
.\venv\scripts\activate.ps1
```

En windows cmd:
```
.\venv\scripts\activate
```

Luego es necesario instalar las dependencias

Instalar dependencias:
```
pip install -r requirements.txt
```

Para crear la base de datos hay que aplicar las migraciones.
Aplicar migraciones:

```
python manage.py migrate
```

Finalmente iniciamos el servidor.
Iniciar servidor:
```
python manage.py runserver
```
Abrir:
http://127.0.0.1:8000/

## Informacion
**Tecnologias**
Este project usa principalmente Python, Django, SQLite y pillow.

**Funcionalidades**
Este blog permite ver posts, registrarse, iniciar y cerrar sesion, CRUD de los posts con imagenes, editar perfil, subir foto de perfil y modificar contraseña.

Solo los usuarios registrados pueden crear posts. Una vez creado el post solo el autor puede modificarlo o eliminarlo.


**Aplicaciones**

- posts: Aplicacion para los posts del blog.
- accounts: Aplicacion para los perfiles y usuarios

**Entrar al panel de admin**
Para entrar al panel de admin primero creamos un superusuario con 
```
python manage.py createsuperuser
```
Ingresamos los datos y luego vamos a /admin/ y entramos con los datos del usuario.

**Carga de imagenes**
La carga de imagenes se puede probar creando un post y subiendo una imagen a dicho post. 

**Autor**
Ignacio Romero

El proyecto usa un placeholder como SECRET_KEY. Nunca usar el placeholder en produccion real.
El proyecto tiene la variable de entorno: DEBUG como True.
No usar este proyecto en produccion real. Si se desea hacerlo asegurese de configurarlo apropiadamente.
Este proyecto fue creado con la ayuda de herramientas IA. 
