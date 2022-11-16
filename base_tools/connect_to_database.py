import psycopg2

HOST = '109.86.215.26'  # 46.172.155.94:53389  109.86.215.26:63389
USER = 'gesheft'
PASSWORD = 'jmgXK4xPXukY'
DB_NAME = 'data_db'
PORT = 63389


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME,
        port=PORT
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")