import sqlite3

def csv_to_db(csv_file, db_file):
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
    print('done')
csv_to_db('../csv_result/result.csv', 'devclub.db')