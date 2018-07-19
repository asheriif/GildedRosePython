import sqlite3

class Database:
	def __init__(self, db_name):
		self.db_name = db_name
		
	def read_database(self):
		connHandle = sqlite3.connect(self.db_name)
		cursorCurrent = connHandle.cursor()
		cursorCurrent.execute('select rowid,* from items')
		resQuery = cursorCurrent.fetchall()
		connHandle.close()
		return resQuery
	
	def update_database(self,items):
		connHandle = sqlite3.connect(self.db_name)
		cursorCurrent = connHandle.cursor()
		for i in range(len(items)):
			cursorCurrent.execute(
			'update items set sell_in=' + str(items[i].sell_in) + ', quality=' + str(items[i].quality) + ' where rowid=' + str(i+1))
		connHandle.commit()
		connHandle.close()
