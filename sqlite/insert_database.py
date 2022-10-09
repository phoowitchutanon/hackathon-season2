import sqlite3
import re
from datetime import datetime
from utils import xml_to_list , Clean_data

datalist = xml_to_list("../data-devclub-1.xml")
datalist = Clean_data(datalist)

def insert_database(xml_file):
    
    data = xml_to_list(xml_file)
    conn = sqlite3.connect('devclub.db')

    c = conn.cursor()

    c.executemany("""INSERT INTO devclub VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",datalist)

    conn.commit()

    conn.close()

if __name__ == "__main__":
    insert_database("../data-devclub-1.xml")