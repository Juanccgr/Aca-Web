# Proyecto Django con Bootstrap

Este proyecto es una aplicación web desarrollada con Django y Bootstrap.

## Requisitos previos

* Python 3.x
* pip (gestor de paquetes de Python)
* Virtualenv (opcional, pero recomendado)

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone URL_DEL_REPOSITORIO
    cd NOMBRE_DEL_PROYECTO
    ```

2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

    (Asegúrate de tener un archivo `requirements.txt` con las dependencias del proyecto).

4.  **Realiza las migraciones de la base de datos:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crea un superusuario (opcional, para acceder al panel de administración):**

    ```bash
    python manage.py createsuperuser
    ```

## Ejecución

1.  **Inicia el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

2.  **Abre el navegador:**

    * Accede a `http://127.0.0.1:8000/` para ver la aplicación.
    * Accede a `http://127.0.0.1:8000/admin/` para acceder al panel de administración (si creaste un superusuario).

## Estructura del proyecto

* `NOMBRE_DEL_PROYECTO/`: Directorio principal del proyecto.
    * `NOMBRE_DEL_PROYECTO/`: Configuración del proyecto.
    * `aplicacion/`: Aplicación Django.
        * `models.py`: Modelos de la base de datos.
        * `views.py`: Vistas de la aplicación.
        * `urls.py`: URLs de la aplicación.
        * `templates/`: Plantillas HTML.
        * `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
    * `venv/`: Entorno virtual (si se creó).
    * `requirements.txt`: Lista de dependencias.
    * `manage.py`: Script de administración de Django.

## Dependencias

* Django
* Bootstrap
* Otras dependencias (listar aquí)
