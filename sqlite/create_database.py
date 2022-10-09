import sqlite3

def create_database():
  conn = sqlite3.connect('devclub.db')

  c = conn.cursor()

  c.execute("""CREATE TABLE devclub (
      EMPID DATATYPE INTEGER,
      PASSPORT DATATYPE TEXT,
      FIRSTNAME DATATYPE TEXT,
      LASTNAME DATATYPE TEXT,
      GENDER DATATYPE TEXT,
      BIRTHDAY DATATYPE DATE,
      NATIONALITY DATATYPE TEXT,
      HIRED DATATYPE DATE,
      DEPT DATATYPE TEXT,
      POSITION DATATYPE TEXT,
      STATUS DATATYPE INTEGER,
      REGION DATATYPE TEXT
      )"""
    )

  c.execute("""CREATE TABLE devclub_backup (
      EMPID DATATYPE INTEGER,
      PASSPORT DATATYPE TEXT,
      FIRSTNAME DATATYPE TEXT,
      LASTNAME DATATYPE TEXT,
      GENDER DATATYPE TEXT,
      BIRTHDAY DATATYPE DATE,
      NATIONALITY DATATYPE TEXT,
      HIRED DATATYPE DATE,
      DEPT DATATYPE TEXT,
      POSITION DATATYPE TEXT,
      STATUS DATATYPE INTEGER,
      REGION DATATYPE TEXT
      )"""
    )
  conn.commit()

  conn.close()

if __name__ == "__main__":
  create_database()