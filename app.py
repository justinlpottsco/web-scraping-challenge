from flask import Flask, render_template
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of our Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Set route
@app.route('/')
def index():
    # Store the mars in a list
    mars = mongo.db.mars.find_one()

# Return the template 
    return render_template('index.html', mars = mars)

@app.route("/scrape")
def scraper():
    mars_scrape = scrape_mars.scrape()
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
