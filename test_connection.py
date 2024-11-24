import psycopg2

try:
    # Intenta conectar a PostgreSQL
    connection = psycopg2.connect(
        host="localhost",              # Host de tu servidor PostgreSQL
        database="PROBANDO2",          # Reemplaza con el nombre de tu base de datos
        user="postgres",               # Usuario de PostgreSQL (por defecto es "postgres")
        password="sql08"        # Reemplaza con tu contraseña de PostgreSQL
    )
    print("Conexión exitosa a PostgreSQL 🎉")
except Exception as e:
    print(f"Error conectando a PostgreSQL: {e}")
finally:
    # Cierra la conexión si fue exitosa
    if 'connection' in locals() and connection:
        connection.close()
