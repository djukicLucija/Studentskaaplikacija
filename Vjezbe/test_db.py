import sqlite3

class Database:
	def __init__(self, db):
		self.connection = sqlite3.connect(db)
		self.cursor = self.connection.cursor()
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS expenses (
				id INTEGER PRIMARY KEY,
				category TEXT,
				amount INTEGER,
				description TEXT
			)
		
		""")
		self.connection.commit()
	
	def insert(self, category:str, amount:int, description:str):
		self.cursor.execute("INSERT INTO expenses VALUES (NULL, ?, ?, ?)", (category, amount, description))
		self.connection.commit()

	def fetch(self):
		self.cursor.execute("SELECT * from expenses")
		return self.cursor.fetchall()
	
	def update(self, id:int, category:str, amount:int, description:str):
		self.cursor.execute("UPDATE expenses SET category=?, amount=?, description=? WHERE id=?", (category, amount, description, id))
		self.connection.commit()

	def delete(self, id:int):
		self.cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
		self.connection.commit()


		
	






