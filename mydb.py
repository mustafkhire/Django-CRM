import psycopg2

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        user='postgres',
        password='1234',
        host='localhost'
    )
    
    # Set autocommit to True
    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE dbmustaf")

    print("Database created successfully")

except psycopg2.Error as e:
    print(f"Error creating database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        # Set autocommit back to False
        connection.autocommit = False
        connection.close()
