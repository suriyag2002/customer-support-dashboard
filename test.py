import mysql.connector

def get_db_connection():
    """Establishes a MySQL database connection."""
    try:
        conn = mysql.connector.connect(
            user="root",  # Use your DB_USER for testing
            password="Suriya@2025",  # Use your DB_PASSWORD for testing
            host="127.0.0.1",  # Use your DB_HOST for testing
            port=3306,  # Use your DB_PORT for testing
            database="day1_db"  # Use your DB_NAME for testing
        )
        print("✅ Database connection successful!")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
        return None

# Testing the connection
conn = get_db_connection()
if conn:
    conn.close()
