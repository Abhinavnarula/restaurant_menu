from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, MenuItem, Restaurant

engine = create_engine('sqlite:///restaurant.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

dbsession = sessionmaker(bind=engine)
session = dbsession()


app = Flask(__name__)


@app.route('/')
@app.route('/restaurant/')
def showRestaurant():
    # return "Restaurants to be displayed here"
    restaurant = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurant=restaurant)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    if(request.method == 'POST'):
        newItem = Restaurant(name=request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    # return "Edit Restaurant here"
    editedItem = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if (request.method == 'POST'):
        if(request.form['name']):
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('editRestaurant.html', restaurant_id=restaurant_id, restaurant_name=editedItem)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    # return "Delete Restaurant here"
    deletedItem = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('deleteRestaurant.html', restaurant_id=restaurant_id, restaurant_name=deletedItem)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def displayMenuItem(restaurant_id):
    # return "Menu items to be displayed here"
    Items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    restaurant_name = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    return render_template('menu.html', items=Items, restaurant=restaurant_name)


@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def addMenuItem(restaurant_id):
    # return "New menu item to be added"
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], description=request.form['description'], price=request.form['price'], course=request.form['course'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('displayMenuItem', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    # return ("MenuItem number %s to be edited here for %s restaurant" % (menu_id, restaurant_id))
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if (request.form['name']):
            editedItem.name = request.form['name']
        if (request.form['name']):
            editedItem.name = request.form['name']
        if (request.form['name']):
            editedItem.name = request.form['name']
    else:
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, editedMenuItem=editedItem)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # return ("MenuItem number %s to be deleted here for %s restaurant", menu_id, restaurant_id)
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, editedMenuItem=editedItem)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
