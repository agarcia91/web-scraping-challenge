#Import dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__, template_folder='template')

#Use flask_pymongo to set up mongo connection 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


#Create the routes
@app.route("/")
def index():
   mars = mongo.db.collections.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape",methods=["GET"])
def scrape():
   mars = mongo.db.mars
   mars_data = scrape_mars.scrape()
   mongo.db.collections.update_one({}, {"$set": mars_data}, upsert=True)
   return redirect ("/")
   




if __name__ == "__main__":
   app.run(debug=True)

