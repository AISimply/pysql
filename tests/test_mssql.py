import os
from dotenv import load_dotenv
import pyodbc

# Load environment variables
load_dotenv("docker/.env")

def connect_to_mssql(server, database, username, password):
    """
    Connects to an MSSQL database and returns the connection object.
    """
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            f"TrustServerCertificate=yes;"
            f"Encrypt=no;"
        )
        conn = pyodbc.connect(connection_string)
        print("Connected to MSSQL database successfully.")
        return conn
    except Exception as e:
        print(f"Failed to connect to MSSQL database: {e}")
        return None

conn = connect_to_mssql(
    server=os.getenv("MSSQL_SERVER", "localhost"),
    database=os.getenv("MSSQL_DATABASE", "tempdb"),
    username=os.getenv("MSSQL_USER", "sa"),
    password=os.getenv("SA_PASSWORD")
)

if conn is None:
    print("Exiting...")
    exit()
cur = conn.cursor()

# Create a table
# Create the table if the table does not exist
if cur.tables(table="test_table", tableType="TABLE").fetchone() is None:
    print("Creating table...")
    cur.execute("CREATE TABLE test_table (id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255))")
else:
    print("Table already exists.") 

# Insert a record
cur.execute("INSERT INTO test_table (name) VALUES ('Chirag')")
conn.commit()

# Select all records
cur.execute("SELECT * FROM test_table")

print(cur.fetchall())

# # Drop the table
# cur.execute("DROP TABLE test_table")

# Close the cursor
cur.close()