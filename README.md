# Blog Django
Projecto Django inicial de un blog
## Descripcion
Repositorio inicial de un blog usando Django
Incluye la configuracion base del proyecto y una app: 'posts'.
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

En Linux o macOS:
```
source venv/bin/activate
```

Instalar dependencias:
```
pip install -r requirements.txt
```

Iniciar servidor:
```
Python manage.py runserver
```
Abrir:
http://127.0.0.1:8000/

**Aplicaciones**

- posts: Aplicacion para los posts del blog.

**Entrar al panel de admin**
Para entrar al panel de admin primero creamos un superusuario con 
```
pyhon manage.py createsuperuser
```
Ingresamos los datos y luego vamos a /admin/ y entramos con los datos del usuario.
