# django-drft-library 
## Sistema de CRUD para Autores y Libros

### Django + Django REST Framework como backend y postgreSQL como base de datos

Estructura del proyecto:
```
.
 ├── README.md
 ├── .env.example
 ├── docker-compose.yml
 ├── Dockerfile
 ├── entrypoint.sh
 ├── deploy.sh
 ├── deploy.cmd
 ├── requirements.txt
 ├── manage.py
 ├── config/
 │   ├── __init__.py
 │   ├── asgi.py
 │   ├── settings.py
 │   ├── urls.py
 │   └── wsgi.py
 ├── library/                    # app principal
 │   ├── __init__.py
 │   ├── fixtures/
 │   │   └── initial_data.json
 │   ├── management
 │   ├── migrations
 │   ├── models
 │   ├── serializers
 │   ├── views
 │   ├── admin.py
 │   ├── apps.py
 │   ├── urls.py
 │   ├── tests.py
 └── .gitignored
 └── .gitattributes
```

[_compose.yaml_](docker-compose.yaml)
```
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      retries: 5

  web:
    build: .
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
    env_file:
    - .env
    volumes:
    ...
```
El archivo define los dos servicios que van a levantarse `web`, `db`.
Al momento de levantar el proyecto, docker compose asigna el puerto 8000 al servicio web del puerto del contenedor al host local como se especifica en el archivo.

Importante!: Verificar que el puerto 8000 ya no este en uso para que funcione correctamente el deploy.

--
### `.env.example`
 ```text
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=your-secret
POSTGRES_DB=books_db
POSTGRES_USER=books_user
POSTGRES_PASSWORD=books_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

## Cómo usar

## Deploy de la aplicacion con docker compose
1. Renombrar el archivo `.env.example` a `.env`.
2. Situarse en el directorio raíz y ejecutar el script dependiendo del entorno:
* Linux, bash : `./deploy.sh up`
* Windows (cmd): `deploy up`
```
$ ./deploy.sh up
Running containers...
[+] Building 21.9s (15/15) FINISHED                        docker:desktop-linux
 => [web internal] load build definition from dockerfile                   0.0s
 => => transferring dockerfile: 592B                                       0.0s
 => [web internal] load metadata for docker.io/library/python:3.11-slim    1.3s

...
[+] Running 4/4
 ✔ Network django-drft-library_default         Created                     0.0s
 ✔ Volume "django-drft-library_postgres_data"  Created                     0.0s
 ✔ Container django-drft-library-db-1          Healthy                     6.1s
 ✔ Container django-drft-library-web-1         Started                     6.3s
Waiting for containers...
.
Deploy completed. Application running on:
  http://localhost:8000/admin/

```
3.  Acceder a `http://localhost:8000/admin/`.

## Verificar estado

Luego de finalizar el deploy, ir a `http://localhost:8000/admin` en tu navegador y verificar que la aplicacion esta corriendo.

## Mejoras futuras

Algunas ideas para seguir mejorando este proyecto:

- **Autenticación y permisos:** Implementar JWT o OAuth2 con `djangorestframework-simplejwt` para proteger los endpoints.
- **Documentación de API:** Agregar Swagger o ReDoc utilizando `drf-spectacular` o `drf-yasg`.
- **Frontend opcional:** Crear una pequeña interfaz en React o Next.js para consumir la API.
- **CI/CD:** Integrar GitHub Actions para testeo y despliegue automático.

## Detener y eliminar los contenedores
Situarse en el directorio raíz y ejecutar el script dependiendo del entorno:
* Linux, bash : `./deploy.sh down`
* Windows (cmd): `deploy down`
```
$ ./deploy.sh down
```
