from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, Restaurant, MenuItem

# interates with database engine
engine = create_engine('sqlite:///restaurant.db')

Base.metadata.bind = engine  # binding the tables
DbSession = sessionmaker(bind=engine)
session = DbSession()

firstRes = Restaurant(name="Pizza hut")
session.add(firstRes)
session.commit()

cheezePizza = MenuItem(name="Cheeze Pizza", description="Made with natural ingredients and fresh mozzarella",
                       course="Entree", price="$8.99", restaurant=firstRes)
session.add(cheezePizza)
session.commit()

print(session.query(Restaurant).all())
print(session.query(MenuItem).all())
