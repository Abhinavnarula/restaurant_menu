from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, MenuItem, Restaurant

engine = create_engine('sqlite:///restaurant.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

dbsession = sessionmaker(bind = engine)
session = dbsession()



app = Flask(__name__)


@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    # return "Restaurants to be displayed here"
    items = session.query(Restaurant).all()
    return render_template('restaurants.html',items = items)


@app.route('/restaurants/new')
def newRestaurant():
    # return "Add new Restaurant here"
    return render_template()


@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "Edit Restaurant here"


@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "Delete Restaurant here"


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def displayMenuItem(restaurant_id):
    return "Menu items to be displayed here"


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def addMenuItem(restaurant_id):
    return "New menu item to be added"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return ("MenuItem number %s to be edited here for %s restaurant" % (menu_id, restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return ("MenuItem number %s to be deleted here for %s restaurant", menu_id, restaurant_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
