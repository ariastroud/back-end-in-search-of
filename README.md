# In Search Of

## Overview
Users can post fashion items they're looking to purchase. If another user has the item that fits the post's specifications, they can email the original poster and make a deal.

The back end of this app was written in Python as a capstone project at [Ada Developers Academy](https://adadevelopersacademy.org/).

##  App Features
![homepage](demo/homepage.png)
* Users can log in with their Google account
![login](demo/login.png)
* Users can post fashion item they're looking for
  * For each post a title, brand, category, size, description and picture can be added
![form](demo/form.png)
![form demo](demo/form_demo.gif)
* Each post has the posting user's email so they can be contacted
* When logged in, users can see all of their items they posted. If the user finds the item they're looking for, they can mark their item as "Found"
![my items](demo/my_items.png)
* Users can search posts by title. 
![search](demo/search.gif)
* Users can filter the search results, their own items and all items by category or size.
![filter](demo/filter.gif)

## Installation
* Clone this repository
* Create a virtual environment `python3 -m venv venv`
* Activate the environment: `source venv/bin/activate`
* Install the dependencies by running `pip install -r requirements.txt`
* Set up the Postgres database
* Clone the [front end](https://github.com/ariastroud/front-end-in-search-of) and follow the instructions on that README
* Start the server by `flask run`   