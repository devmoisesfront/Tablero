from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os
import subprocess
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar mensajes flash

# Leer scripts de la carpeta scripts
def get_scripts():
    try:
        script_files = [f for f in os.listdir('scripts') if f.endswith('.py')]
        scripts = [{'script_name': os.path.splitext(f)[0]} for f in script_files]
        return scripts
    except Exception as e:
        flash(f"Error al leer scripts: {str(e)}", "error")
        return []

# Inicializar archivo CSV
def initialize_status_file(scripts):
    try:
        if not os.path.exists('update_status.csv'):
            df = pd.DataFrame(scripts)
            df['last_run'] = (datetime.now() - pd.DateOffset(days=2)).strftime('%Y-%m-%d %H:%M:%S')  # Fecha de hace 2 días para simular desactualización
            df.to_csv('update_status.csv', index=False)
    except Exception as e:
        flash(f"Error al inicializar el archivo de estado: {str(e)}", "error")

# Actualizar el archivo CSV con los scripts nuevos
def update_status_file():
    try:
        scripts = get_scripts()
        if scripts:  # Verificar si hay scripts
            if os.path.exists('update_status.csv'):
                df_existing = pd.read_csv('update_status.csv')
                df_new = pd.DataFrame(scripts)
                df = pd.merge(df_new, df_existing, on='script_name', how='left')
                df['last_run'] = df['last_run'].fillna((datetime.now() - pd.DateOffset(days=2)).strftime('%Y-%m-%d %H:%M:%S'))
                df.to_csv('update_status.csv', index=False)
            else:
                initialize_status_file(scripts)
        else:
            if os.path.exists('update_status.csv'):
                os.remove('update_status.csv')  # Eliminar archivo de estado si no hay scripts
            flash("La carpeta de scripts está vacía. Ingrese su primer script.", "warning")
    except Exception as e:
        flash(f"Error al actualizar el archivo de estado: {str(e)}", "error")

# Leer el estado de los scripts
def read_status():
    try:
        return pd.read_csv('update_status.csv')
    except FileNotFoundError:
        flash("Error: No se encontró el archivo de estado.", "error")
        return pd.DataFrame()
    except Exception as e:
        flash(f"Error al leer el archivo de estado: {str(e)}", "error")
        return pd.DataFrame()

# Actualizar el estado de los scripts
def update_status(script_name):
    try:
        df = read_status()
        df.loc[df['script_name'] == script_name, 'last_run'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df.to_csv('update_status.csv', index=False)
    except Exception as e:
        flash(f"Error al actualizar el estado del script: {str(e)}", "error")

# Ejecutar un script
def run_script(script_name):
    script_path = os.path.join('scripts', f'{script_name}.py')
    if os.path.exists(script_path):
        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            if result.returncode == 0:
                update_status(script_name)
                flash(f"{script_name} ejecutado con éxito.", "success")
            else:
                flash(f"Error ejecutando {script_name}: {result.stderr}", "error")
        except Exception as e:
            flash(f"Error al ejecutar el script {script_name}: {str(e)}", "error")
    else:
        flash(f"Error: {script_path} no encontrado.", "error")

@app.route('/')
def index():
    update_status_file()  # Actualizar la lista de scripts cada vez que se accede a la página principal
    df = read_status()
    scripts_status = []

    if df.empty:
        flash("La carpeta de scripts está vacía. Ingrese su primer script.", "warning")
    else:
        try:
            for index, row in df.iterrows():
                last_run = datetime.strptime(row['last_run'], '%Y-%m-%d %H:%M:%S')
                now = datetime.now()
                status = 'Actualizado' if (now - last_run).days < 1 else 'Desactualizado'
                status_color = 'green' if status == 'Actualizado' else 'red'
                scripts_status.append({
                    'script_name': row['script_name'],
                    'last_run': row['last_run'],
                    'status': status,
                    'status_color': status_color
                })
        except Exception as e:
            flash(f"Error al procesar el estado de los scripts: {str(e)}", "error")

    return render_template('index.html', scripts_status=scripts_status)

@app.route('/run_script/<script_name>', methods=['POST'])
def execute_script(script_name):
    run_script(script_name)
    return redirect(url_for('index'))

@app.route('/update_scripts')
def update_scripts():
    update_status_file()
    flash("Lista de scripts actualizada.", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
