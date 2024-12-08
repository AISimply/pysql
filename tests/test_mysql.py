import os
import mysql.connector as sql
from dotenv import load_dotenv

# Load environment variables
load_dotenv("docker/.env")

conn = sql.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cur = conn.cursor()

# Create a table
# Create the table if the table does not exist
cur.execute("SHOW TABLES LIKE 'test_table'")
result = cur.fetchone()
if result is None:
    print("Creating table...")
    cur.execute("CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
else:
    print("Table already exists.")

# Insert a record
cur.execute("INSERT INTO test_table (name) VALUES ('Chirag')")
conn.commit()

# Select all records
cur.execute("SELECT * FROM test_table")
# commit the transaction
print(cur.fetchall())

# # Drop the table
# cur.execute("DROP TABLE test_table")
# print(cur.fetchall())

# Close the cursor
cur.close()