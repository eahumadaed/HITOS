# Proyecto Django - Hito 2: Creación de un sitio web responsive con Bootstrap

## Descripción

En este proyecto, continuaremos personalizando el sitio web OnlyFlans utilizando Bootstrap para crear un sitio web responsive y atractivo.

## Requerimientos

### 1. Crear una nueva aplicación Django
- Inicia una nueva app de Django llamada `web` dentro del proyecto `onlyflans`.
- Agrega la app `web` a la lista de aplicaciones instaladas.
- Crea una carpeta `templates` dentro de la app `web` y añade un archivo `index.html` con las estructuras `<html>`, `<header>`, y `<body>` que contenga el texto "índice".
- Crea 2 copias del archivo `index.html`, nombradas `about.html` y `welcome.html`, reemplazando el texto del `<body>` por "acerca" y "bienvenido cliente" respectivamente.

### 2. Habilitar URLs
- Configura las rutas para que muestren los textos básicos:
  - Ruta `/`: muestra el texto "índice".
  - Ruta `/acerca`: muestra el texto "acerca".
  - Ruta `/bienvenido`: muestra el texto "bienvenido cliente".
- Ejecuta el servidor de desarrollo con `python manage.py runserver` y captura pantallazos de cada ruta.

### 3. Crear una plantilla base
- Crea una plantilla base llamada `base.html` que incluya los elementos comunes:
  - `header`
  - `navbar`
  - `footer`
- Usa `<div>` con colores de fondo para separar y visualizar mejor los elementos.
- Extiende `base.html` en las plantillas de las rutas y captura pantallazos de cada una.

### 4. Personalizar las vistas y plantillas
- Incluye Bootstrap en la plantilla base.
- Actualiza el título de la página a "Bienvenido a onlyflans".
- Agrega la clase CSS `container` a los elementos principales para una mejor disposición.
- Reemplaza los contenidos de `header`, `navbar`, y `footer` por componentes de Bootstrap y usa plantillas para cada componente:
  - `header.html`
  - `navbar.html`
  - `footer.html`
- Asegúrate de que el `navbar` tenga enlaces a cada una de las URLs.
- Captura pantallazos de cada ruta.

