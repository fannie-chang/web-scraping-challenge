from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.mars_db

# create route that renders index.html template

@app.route("/")
def index():
	mars_data = mongo.db.mars_data.find_one()
	return render_template("index.html" , mars_data = mars_data)




@app.route("/scrape")
def scrape_info():
	mars_data = mongo.db.mars_data
	mars_data = scrape_mars.scrape()
	mars_data.update({},mars_data, upsert=True )
	return redirect ("/")




if __name__=="__main__":
	app.run(debug=True)

	 