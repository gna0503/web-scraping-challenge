from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import app_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# clear mongo
mongo.db.collection.drop()

@app.route("/")
def home():
    
    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()
    
    # Return template and data
    #print(destination_data)
    return render_template("index.html", news=destination_data)


@app.route("/scrape")
def scraper():
    
    
    #collection = mongo.db.collection
    
    # Run the scrape function
    scrape_data = app_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scrape_data, upsert=True)
    
    # insert new document
    #mongo.db.collection.insert_one(scrape_data)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)