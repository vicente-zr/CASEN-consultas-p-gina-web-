from flask import render_template, request, current_app  # Usa current_app en lugar de app
from . import db

@current_app.route('/')
def index():
    return "¡RENUNCIA GARECA!"

@current_app.route('/consulta1', methods=['GET', 'POST'])
def consulta1():
    resultados = None
    if request.method == 'POST':
        tipo_vivienda = request.form.get('tipo_vivienda')
        resultados = db.session.execute(
            '''
            SELECT 
                h.tipo_vivienda, 
                COUNT(p.id_persona) AS total_personas
            FROM hogares h
            JOIN personas p ON h.id_hogar = p.id_hogar
            WHERE h.tipo_vivienda = :tipo_vivienda
            GROUP BY h.tipo_vivienda
            ''', {'tipo_vivienda': tipo_vivienda}
        ).fetchall()
    return render_template('consulta1.html', resultados=resultados)


from sqlalchemy.sql import text
from flask import current_app
from . import db

@current_app.route('/check_db')
def check_db():
    try:
        # Usa text() para consultas explícitas
        result = db.session.execute(text('SELECT 1')).fetchall()
        return "Conexión a la base de datos exitosa 🎉"
    except Exception as e:
        return f"Error conectando a la base de datos: {e}"


from flask import render_template
from sqlalchemy.sql import text
from . import db


from flask import render_template, current_app
from . import db
from sqlalchemy.sql import text

@current_app.route('/ver_hogares')
def ver_hogares():
    try:
        resultados = db.session.execute(text("SELECT * FROM hogares")).fetchall()
        # Devuelve los datos directamente en texto
        return str(resultados)
    except Exception as e:
        return f"Error al consultar hogares: {e}"
    

@current_app.route('/tabla_hogares')
def tabla_hogares():
    try:
        # Ejecuta la consulta para obtener datos de la tabla 'hogares'
        query = text("SELECT id_hogar, tipo_vivienda, n_personas_vivienda, presupuesto_compartido FROM hogares")
        resultados = db.session.execute(query).fetchall()

        # Construir la tabla en HTML directamente
        tabla_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla de Hogares</title>
            <style>
                table {
                    width: 80%;
                    border-collapse: collapse;
                    margin: 25px auto;
                    font-size: 18px;
                    text-align: left;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">Tabla de Hogares</h1>
            <table>
                <tr>
                    <th>ID Hogar</th>
                    <th>Tipo de Vivienda</th>
                    <th>Número de Personas</th>
                    <th>Presupuesto Compartido</th>
                </tr>
        """
        for fila in resultados:
            tabla_html += f"""
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                </tr>
            """
        tabla_html += """
            </table>
        </body>
        </html>
        """
        return tabla_html
    except Exception as e:
        return f"Error generando la tabla: {e}"


@current_app.route('/tabla_personas')
def tabla_personas():
    try:
        query = text("SELECT id_persona, id_hogar, sexo, edad FROM personas")
        resultados = db.session.execute(query).fetchall()

        tabla_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla de Personas</title>
            <style>
                table {
                    width: 80%;
                    border-collapse: collapse;
                    margin: 25px auto;
                    font-size: 18px;
                    text-align: left;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">Tabla de Personas</h1>
            <table>
                <tr>
                    <th>ID Persona</th>
                    <th>ID Hogar</th>
                    <th>Sexo</th>
                    <th>Edad</th>
                </tr>
        """
        for fila in resultados:
            tabla_html += f"""
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                </tr>
            """
        tabla_html += """
            </table>
        </body>
        </html>
        """
        return tabla_html
    except Exception as e:
        return f"Error generando la tabla: {e}"


@current_app.route('/tabla_educacion')
def tabla_educacion():
    try:
        query = text("SELECT id_persona, id_hogar, asiste_educacion, nivel_educacional, dependencia_establecimiento FROM educacion")
        resultados = db.session.execute(query).fetchall()

        tabla_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla de Educación</title>
            <style>
                table {
                    width: 80%;
                    border-collapse: collapse;
                    margin: 25px auto;
                    font-size: 18px;
                    text-align: left;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">Tabla de Educación</h1>
            <table>
                <tr>
                    <th>ID Persona</th>
                    <th>ID Hogar</th>
                    <th>Asiste Educación</th>
                    <th>Nivel Educacional</th>
                    <th>Dependencia</th>
                </tr>
        """
        for fila in resultados:
            tabla_html += f"""
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                    <td>{fila[4]}</td>
                </tr>
            """
        tabla_html += """
            </table>
        </body>
        </html>
        """
        return tabla_html
    except Exception as e:
        return f"Error generando la tabla: {e}"

@current_app.route('/tabla_trabajo')
def tabla_trabajo():
    try:
        query = text("SELECT id_persona, id_hogar, ocupacion, tipo_contrato, horas_trabajadas FROM trabajo")
        resultados = db.session.execute(query).fetchall()

        tabla_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tabla de Trabajo</title>
            <style>
                table {
                    width: 80%;
                    border-collapse: collapse;
                    margin: 25px auto;
                    font-size: 18px;
                    text-align: left;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <h1 style="text-align: center;">Tabla de Trabajo</h1>
            <table>
                <tr>
                    <th>ID Persona</th>
                    <th>ID Hogar</th>
                    <th>Ocupación</th>
                    <th>Tipo de Contrato</th>
                    <th>Horas Trabajadas</th>
                </tr>
        """
        for fila in resultados:
            tabla_html += f"""
                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2]}</td>
                    <td>{fila[3]}</td>
                    <td>{fila[4]}</td>
                </tr>
            """
        tabla_html += """
            </table>
        </body>
        </html>
        """
        return tabla_html
    except Exception as e:
        return f"Error generando la tabla: {e}"


@current_app.route('/cantidad_personas', methods=['GET', 'POST'])
def cantidad_personas():
    if request.method == 'POST':
        tipo_vivienda = request.form.get('tipo_vivienda')
        print(f"Tipo de vivienda recibido: {tipo_vivienda}")  # Depuración en terminal
        try:
            query = text("""
                SELECT h.tipo_vivienda, 
                       COUNT(p.id_persona) AS total_personas
                FROM hogares h
                JOIN personas p ON h.id_hogar = p.id_hogar
                WHERE h.tipo_vivienda = :tipo_vivienda
                GROUP BY h.tipo_vivienda
            """)
            resultados = db.session.execute(query, {"tipo_vivienda": tipo_vivienda}).fetchall()
            print(f"Resultados de la consulta: {resultados}")  # Depuración
            return render_template('cantidad_personas.html', resultados=resultados, tipo_vivienda=tipo_vivienda)
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")  # Depuración de errores
            return f"Error ejecutando la consulta: {e}"
    return render_template('cantidad_personas_form.html')

@current_app.route('/cantidad_personas_compleja', methods=['GET', 'POST'])
def cantidad_personas_compleja():
    if request.method == 'POST':
        tipo_vivienda = request.form.get('tipo_vivienda')
        tipo_contrato = request.form.get('tipo_contrato')
        print(f"Tipo de vivienda recibido: {tipo_vivienda}")  # Depuración en terminal
        print(f"Tipo de contrato recibido: {tipo_contrato}")  # Depuración en terminal
        try:
            query = text("""
                SELECT 
                    h.tipo_vivienda,
                    COUNT(DISTINCT p.id_persona) AS total_personas,
                    t.tipo_contrato
                FROM 
                    hogares h
                JOIN 
                    personas p ON h.id_hogar = p.id_hogar
                JOIN 
                    trabajo t ON p.id_hogar = t.id_hogar AND p.id_persona = t.id_persona
                WHERE 
                    h.tipo_vivienda = :tipo_vivienda
                    AND t.tipo_contrato = :tipo_contrato
                GROUP BY 
                    h.tipo_vivienda, t.tipo_contrato;
            """)
            resultados = db.session.execute(query, {"tipo_vivienda": tipo_vivienda, "tipo_contrato": tipo_contrato}).fetchall()
            print(f"Resultados de la consulta: {resultados}")  # Depuración
            return render_template('cantidad_personas_compleja.html', resultados=resultados, tipo_vivienda=tipo_vivienda, tipo_contrato=tipo_contrato)
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")  # Depuración de errores
            return f"Error ejecutando la consulta: {e}"
    return render_template('cantidad_personas_compleja_form.html')




@current_app.route('/promedio_horas', methods=['GET', 'POST'])
def promedio_horas():
    if request.method == 'POST':
        nivel_educacional = request.form.get('nivel_educacional')
        print(f"Nivel educacional recibido: {nivel_educacional}")  # Depuración en terminal
        try:
            query = text("""
                SELECT e.nivel_educacional, 
                       AVG(CAST(NULLIF(t.horas_trabajadas, '') AS INTEGER)) AS promedio_horas_trabajadas
                FROM educacion e
                JOIN trabajo t ON e.id_hogar = t.id_hogar AND e.id_persona = t.id_persona
                WHERE e.nivel_educacional = :nivel_educacional
                  AND t.horas_trabajadas ~ '^[0-9]+$'  -- Solo valores numéricos
                GROUP BY e.nivel_educacional
            """)
            resultados = db.session.execute(query, {"nivel_educacional": nivel_educacional}).fetchall()
            print(f"Resultados de la consulta: {resultados}")  # Depuración
            return render_template('promedio_horas.html', resultados=resultados, nivel_educacional=nivel_educacional)
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")  # Depuración de errores
            return f"Error ejecutando la consulta: {e}"
    return render_template('promedio_horas_form.html')



@current_app.route('/personas_sin_ocupacion', methods=['GET', 'POST'])
def personas_sin_ocupacion():
    if request.method == 'POST':
        edad_min = request.form.get('edad_min', 0)  # Edad mínima, por defecto 0
        edad_max = request.form.get('edad_max', 40)  # Edad máxima, por defecto 40
        print(f"Rango de edades recibido: {edad_min} - {edad_max}")  # Depuración en terminal
        try:
            query = text("""
                SELECT 
                    p.id_hogar,
                    p.id_persona,
                    p.edad,
                    t.ocupacion,
                    t.tipo_contrato
                FROM 
                    personas p
                JOIN 
                    trabajo t ON p.id_hogar = t.id_hogar AND p.id_persona = t.id_persona
                WHERE 
                    t.ocupacion = 'Desconocido' 
                    AND t.tipo_contrato = 'Sin contrato'
                    AND p.edad ~ '^[0-9]+$'  -- Filtrar solo valores numéricos para edad
                    AND CAST(NULLIF(p.edad, '') AS INTEGER) BETWEEN :edad_min AND :edad_max;
            """)
            resultados = db.session.execute(query, {"edad_min": edad_min, "edad_max": edad_max}).fetchall()
            print(f"Resultados de la consulta: {resultados}")  # Depuración
            return render_template('personas_sin_ocupacion.html', resultados=resultados, edad_min=edad_min, edad_max=edad_max)
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")  # Depuración de errores
            return f"Error ejecutando la consulta: {e}"
    return render_template('personas_sin_ocupacion_form.html')
