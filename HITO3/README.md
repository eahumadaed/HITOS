# Proyecto Django - Hito 3: Añadiendo Interacción a Nuestro Sitio Web

## Descripción

En este proyecto, agregaremos interacción al sitio web OnlyFlans utilizando Django y Bootstrap. Crearemos modelos y formularios para mejorar la funcionalidad del sitio y permitir la interacción con los usuarios.

## Requerimientos

### 1. Crear el Modelo Flan
- Crear un modelo llamado `Flan` con los siguientes atributos:
  - `flan_uuid` del tipo `UUIDField`
  - `name` del tipo `CharField` (largo máximo 64 caracteres)
  - `description` del tipo `TextField`
  - `image_url` del tipo `URLField`
  - `slug` del tipo `SlugField`
  - `is_private` del tipo `BooleanField`
- Generar y aplicar las migraciones.
- Registrar el modelo en el panel de administración.
- Crear al menos 8 flanes en el panel de administración.

![Snap 2024-06-06 at 00.15.23](IMAGENES/Snap%202024-06-06%20at%2000.15.23.png)
![Snap 2024-06-06 at 00.15.42](IMAGENES/Snap%202024-06-06%20at%2000.15.42.png)
![Snap 2024-06-06 at 00.17.17](IMAGENES/Snap%202024-06-06%20at%2000.17.17.png)
![Snap 2024-06-06 at 00.22.59](IMAGENES/Snap%202024-06-06%20at%2000.22.59.png)


### 2. Mostrar los Flanes en el Sitio Web
- Añadir los flanes a la vista de la ruta `/` (Index) y mostrar los resultados en la plantilla `index.html` utilizando Bootstrap.
- Mostrar los flanes privados en la página de bienvenida (`/bienvenido`).

![Snap 2024-06-06 at 00.24.15](IMAGENES/Snap%202024-06-06%20at%2000.24.15.png)
![Snap 2024-06-06 at 00.24.31](IMAGENES/Snap%202024-06-06%20at%2000.24.31.png)



### 3. Crear el Modelo ContactForm
- Crear un modelo llamado `ContactForm` con los siguientes atributos:
  - `contact_form_uuid` del tipo `UUIDField` (valor por defecto `uuid.uuid4`, no editable)
  - `customer_email` del tipo `EmailField`
  - `customer_name` del tipo `CharField` (largo máximo 64 caracteres)
  - `message` del tipo `TextField`
- Generar y aplicar las migraciones.
- Registrar el modelo en el panel de administración.

![Snap 2024-06-06 at 00.24.56](IMAGENES/Snap%202024-06-06%20at%2000.24.56.png)
![Snap 2024-06-06 at 00.25.11](IMAGENES/Snap%202024-06-06%20at%2000.25.11.png)
![Snap 2024-06-06 at 00.25.25](IMAGENES/Snap%202024-06-06%20at%2000.25.25.png)
![Snap 2024-06-06 at 00.25.38](IMAGENES/Snap%202024-06-06%20at%2000.25.38.png)




### 4. Crear Formulario de Contacto
- Crear un formulario en `forms.py`.
- Crear una vista para manejar el formulario en `views.py`.
- Crear las plantillas `contact.html` y `exito.html`.

![Snap 2024-06-06 at 00.25.56](IMAGENES/Snap%202024-06-06%20at%2000.25.56.png)
![Snap 2024-06-06 at 00.26.07](IMAGENES/Snap%202024-06-06%20at%2000.26.07.png)

### 5. Modificaciones Finales
- Estilizar el formulario de contacto para mostrar los campos individualmente.
- Modificar la plantilla de la ruta `/acerca` para describir el propósito del sitio web.
- Generar los siguientes pantallazos y guardarlos en formato jpg o png:
  - Página Inicio
  - Página Bienvenido
  - Página Acerca
  - Página Contacto (sin datos)
  - Página Contacto (con correo erróneo)
  - Página Contacto (con correo correcto)
  - Página de éxito luego de enviar un contacto
  - Detalle del contacto creado en el panel de administración de Django


![Snap 2024-06-06 at 00.32.26](IMAGENES/Snap%202024-06-06%20at%2000.32.26.png)
![Snap 2024-06-06 at 00.32.55](IMAGENES/Snap%202024-06-06%20at%2000.32.55.png)
![Snap 2024-06-06 at 00.33.21](IMAGENES/Snap%202024-06-06%20at%2000.33.21.png)
![Snap 2024-06-06 at 00.33.38](IMAGENES/Snap%202024-06-06%20at%2000.33.38.png)
![Snap 2024-06-06 at 00.34.03](IMAGENES/Snap%202024-06-06%20at%2000.34.03.png)

### FIN