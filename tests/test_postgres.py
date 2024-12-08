import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv("docker/.env")

conn = psycopg2.connect(
    host="localhost",
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    database=os.getenv("POSTGRES_DATABASE")
)

cur = conn.cursor()

# Create a table
# Create the table if the table does not exist
cur.execute("SELECT * FROM information_schema.tables WHERE table_name='test_table'")
if cur.rowcount == 0:
    print("Creating table...")
    cur.execute("CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(255))")
else:
    print("Table already exists.")

# Insert a record
cur.execute("INSERT INTO test_table (name) VALUES ('Vincent')")
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