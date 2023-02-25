import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Create a table with a timestamp field
c.execute('''CREATE TABLE mytable
             (id INTEGER PRIMARY KEY,
              name TEXT,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Insert a row into the table with the current timestamp
c.execute("INSERT INTO mytable (name) VALUES ('John Doe')")

# Retrieve the row from the table and print the timestamp
result = c.execute("SELECT * FROM mytable WHERE name='John Doe'")
row = result.fetchone()
print(row[2])  # prints the value of the 'created_at' field
