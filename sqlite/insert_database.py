import sqlite3
import re
from datetime import datetime

def xml_to_list(xml_file):
    props = ["EMPID","PASSPORT","FIRSTNAME","LASTNAME","GENDER","BIRTHDAY","NATIONALITY","HIRED","DEPT","POSITION"]

    with open(xml_file) as f:
      data = f.read()

    datalist = []
    for prop in props:
        data_prop = re.findall(rf"<{prop}>(.*?)</{prop}>", data)
        if prop in ["HIRED","BIRTHDAY"]:
          data_prop = [datetime.strptime(datestring, '%d-%m-%Y').strftime('%Y-%m-%d') for datestring in data_prop]
        datalist.append(data_prop)
    datalist = list(zip(*datalist))
    return datalist

def insert_database(xml_file):
    
    data = xml_to_list(xml_file)
    conn = sqlite3.connect('devclub.db')

    c = conn.cursor()

    c.executemany("""INSERT INTO devclub VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",data)

    conn.commit()

    conn.close()

if __name__ == "__main__":
    insert_database("../data-devclub-1.xml")