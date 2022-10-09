import sqlite3
import json



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

if __name__ == "__main__":
    sqlite_to_json('devclub.db')