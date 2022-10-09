import sqlite3

def query_database():
  
  conn = sqlite3.connect('devclub.db')

  c = conn.cursor()

  c.execute("SELECT * FROM devclub")

  items = c.fetchall()
  for item in items:
    print(item)

  conn.commit()

  conn.close()

if __name__ == "__main__":
  query_database()