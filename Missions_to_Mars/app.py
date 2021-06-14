from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# create route that renders index.html template

@app.route("/")
def index():
	mars_data = mongo.db.mars_data.find_one()
	return render_template("index.html" , mars_data = mars_data)
def table():
	return render_template("mars_facts.html")



@app.route("/scrape")
def scrape():

	mars = mongo.db.mars_data
	mars_data = scrape_mars.scrape()
	mars.update({},mars_data, upsert=True )
	return redirect("/", code =302)


if __name__=="__main__":
	app.run(debug=True)

	 