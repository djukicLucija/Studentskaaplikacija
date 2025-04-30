import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS studenti(
            id Integer Primary Key,
            ime text,
            indeks text,
            predmet text,
            ocjena text 
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, ime, indeks, predmet, ocjena):
        self.cur.execute("insert into studenti values (NULL,?,?,?,?)",
                         (ime, indeks, predmet, ocjena))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from studenti")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, indeks):
        self.cur.execute("delete from studenti where indeks=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, indeks, ime, predmet, ocjena):
        self.cur.execute(
            "update studenti set ime=?, indeks=?, predmet=?, ocjena=? where id=?",
            (ime, indeks, predmet, ocjena,id))
        self.con.commit()

