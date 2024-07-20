
README para el Gestor de Scripts
Gestor de Scripts
El Gestor de Scripts es una aplicación web que permite la gestión y ejecución de scripts de manera sencilla y eficiente. La interfaz está diseñada para mostrar el estado actual de los scripts, su última ejecución y proporcionar opciones para actualizarlos o ejecutarlos manualmente.

Características
Visualización de scripts: Muestra una lista de scripts con su nombre, última ejecución y estado.
Ejecución de scripts: Permite ejecutar scripts manualmente a través de un botón en la interfaz.
Actualización de lista de scripts: Opción para actualizar la lista de scripts mostrada en la interfaz.
Mensajes de estado: Notificaciones para informar sobre el éxito o fallo de las operaciones.
Requisitos
Python 3.12
Flask
Bootstrap 4.5.2
Instalación
Clonar el repositorio:

bash
Copiar código
git clone git@github.com:devmoisesfront/Tablero.git
cd Tablero
Crear un entorno virtual y activarlo:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instalar las dependencias:

bash
Copiar código
pip install -r requirements.txt
Uso
Ejecutar la aplicación Flask:

bash
Copiar código
flask run
Abrir un navegador web y navegar a http://127.0.0.1:5000 para ver la aplicación en acción.

Estructura del Proyecto
app.py: Archivo principal que contiene la lógica de la aplicación Flask.
templates/: Directorio que contiene las plantillas HTML.
index.html: Plantilla principal para la interfaz del Gestor de Scripts.
static/: Directorio que contiene archivos estáticos como CSS y JavaScript.
Personalización
Actualización de Scripts
Para actualizar la lista de scripts, puedes definir la lógica en la función update_scripts en app.py. Esta función debe encargarse de obtener la información de los scripts y actualizar el estado en la interfaz.

Ejecución de Scripts
La ejecución de scripts se maneja en la función execute_script en app.py. Aquí puedes añadir la lógica necesaria para ejecutar los scripts de acuerdo a tus necesidades.

Footer
El pie de página de la aplicación incluye información de copyright y el autor:

html
Copiar código
<footer>
    &copy; 2024 Marca registrada y desarrollado e implementado por <a href="https://devmoisesfront.github.io/Portafolio/" target="_blank">Moisés Caez</a>
</footer>
Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza los cambios necesarios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Crea un nuevo Pull Request.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Si tienes alguna pregunta o sugerencia, no dudes en contactar al desarrollador en el portafolio de Moisés Caez.
