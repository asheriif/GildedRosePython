from flask import Flask,render_template
from gilded_rose import Item,GildedRose
from database import Database
app = Flask(__name__)

## CODE DUPLICATED. NEEDS REFACTORING. 
@app.route("/")
def hello():
	database = Database("database.db")
	items = []
	res = database.read_database()
	for item in res:
		items.append(Item(item[1],item[2],item[3]))
	gilded_rose = GildedRose(items)
	return render_template('index.html',**locals())

@app.route("/update")
def update():
	database = Database("database.db")
	items = []
	res = database.read_database()
	for item in res:
		items.append(Item(item[1],item[2],item[3]))
	gilded_rose = GildedRose(items)
	gilded_rose.update_quality()
	return render_template('index.html',**locals())

if __name__ == "__main__":
    app.run()
