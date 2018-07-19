import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE items (name TEXT, sell_in INT, quality INT)')
print ("Table created successfully")

conn.execute('INSERT INTO items values ("Aged Brie",11,10);')
conn.execute('INSERT INTO items values ("Sulfuras, Hand of Ragnaros",11,80);')
conn.execute('INSERT INTO items values ("Backstage passes to a TAFKAL80ETC concert",11,10);')
conn.execute('INSERT INTO items values ("Conjured",11,10);')
conn.execute('INSERT INTO items values ("Aged Brie",11,10);')
conn.execute('INSERT INTO items values ("Sulfuras, Hand of Ragnaros",11,80);')
conn.execute('INSERT INTO items values ("Conjured",11,10);'	)
conn.execute('INSERT INTO items values ("Backstage passes to a TAFKAL80ETC concert",11,10);')
conn.commit()

print ("Dummy values inserted.")
conn.close()
