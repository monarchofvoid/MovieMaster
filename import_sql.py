import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Read the SQL file
with open('moviesdatabase.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit and close
conn.commit()
conn.close()

print("Database import completed successfully.")
