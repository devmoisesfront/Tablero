# Tablero de Control

Este proyecto es un tablero de control desarrollado para gestionar y visualizar actualizaciones diarias de datos. El tablero muestra banderas verdes si los datos están actualizados correctamente.

## Descripción

El Tablero de Control es una herramienta diseñada para analistas de datos e ingenieros, permitiendo una gestión eficiente de las actualizaciones diarias. Utiliza Python para ejecutar scripts y verificar el estado de los datos, presentando la información de una manera clara y visual.

## Características

- **Ejecución de scripts:** Permite ejecutar scripts automáticamente.
- **Verificación de actualizaciones:** Muestra banderas verdes si los datos están actualizados.
- **Visualización clara:** Interfaz amigable y fácil de usar para visualizar el estado de las actualizaciones.

## Requisitos

- Python 3.12
- Bibliotecas necesarias (ver `requirements.txt`)

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/devmoisesfront/Tablero.git

   cd Tablero
pip install -r requirements.txt
python main.py

   ```sh
Tablero/
│
├── data/                 # Directorio para almacenar los datos
│
├── scripts/              # Scripts de actualización y verificación
│
├── static/               # Archivos estáticos (CSS, imágenes, etc.)
│
├── templates/            # Plantillas HTML para la interfaz
│
├── main.py               # Script principal para ejecutar el tablero
│
├── requirements.txt      # Archivo de dependencias
│
└── README.md             # Este archivo

