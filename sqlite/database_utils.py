import sqlite3
from utils import xml_to_list , Clean_data
import json

def create_database(db_name):
  conn = sqlite3.connect(db_name)

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

def csv_to_database(csv_file, db_file):

    with open(csv_file, 'r') as f:
        data = f.read()
    datalist = data.split('\n')[1:-1]
    datalist = list(tuple(x.split(',')) for x in datalist)
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS devclub (
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
      REGION DATATYPE TEXT)"""
    )
  
    c.executemany("""INSERT INTO devclub VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",datalist)
    conn.commit()
    conn.close()

def create_view():
    conn = sqlite3.connect('devclub.db')
    c = conn.cursor()
    c.execute("""CREATE VIEW devclub_view AS SELECT * FROM devclub""")
    conn.commit()
    conn.close()

def insert_database(xml_file):
    
    datalist = xml_to_list(xml_file)

    datalist = Clean_data(datalist)

    conn = sqlite3.connect('devclub.db')

    c = conn.cursor()

    c.executemany("""INSERT INTO devclub VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",datalist)

    conn.commit()

    conn.close()

def sqlite_to_json(db_file):
    props = ["EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY",
             "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"]
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM devclub")
    items = c.fetchall()

    datadict = {}
    for index,item in enumerate(items):
        key = index
        datadict[key] = dict(zip(props, item))
    conn.commit()
    conn.close()

    print(datadict)
    with open('data_from_sqlite.json', 'w') as f:
        json.dump(datadict, f, indent=4)

def query_database():
  
  conn = sqlite3.connect('devclub.db')

  c = conn.cursor()

  c.execute("SELECT * FROM devclub")

  items = c.fetchall()
  for item in items:
    print(item)

  conn.commit()

  conn.close()