#from sqlalchemy import Integer, String
#from sqlalchemy.orm import mapped_column, Mapped
#import sqlalchemy as sa #sa.Column


"""  class cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique =True, nullable=True)
    map_url : Mapped[str] = mapped_column(String(250), nullable=True)
    img_url : Mapped[str] = mapped_column(String(250), nullable=True)
    location : Mapped[str] = mapped_column(String(250), nullable=True)
    has_sockets : Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet : Mapped[str] = mapped_column(String(250), nullable=True)
    has_wifi : Mapped[str] = mapped_column(String(250), nullable=True)
    can_take_calls : Mapped[str] = mapped_column(String(250), nullable=True)
    seats : Mapped[str] = mapped_column(String(250), nullable=True)
    coffee_price  : Mapped[str] = mapped_column(String(250), nullable=True) """

""" 
    #db.reflect()#initialise a class with the table's database
    
    #cafes = db.session.execute(select(Cafe))
#class correspond to the the table in the db
class Cafe(db.Model):
    __table__ = db.metadata.tables["cafe"]
 """

#-------------------------------sqlalchemy work------------------------------

""" import sqlalchemy as db


#initilase db connection
engine = db.create_engine('sqlite:///cafes.db')
conn = engine.connect()
metadata = db.MetaData()
t_cafe = db.Table('cafe', metadata, autoload_with=engine)
#print(t_cafe.columns.keys())

#select all
query = t_cafe.select()
exe = conn.execute(query)
result = exe.all()

for r in result:
    list_cafes.append(r._data)

for r in list_cafes:
    print(r)

 """


#-------------------------------------
#flask_sqlalchemy

""" class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique =True, nullable=True)
    map_url : Mapped[str] = mapped_column(String(250), nullable=True)
    img_url : Mapped[str] = mapped_column(String(250), nullable=True)
    location : Mapped[str] = mapped_column(String(250), nullable=True)
    has_sockets : Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet : Mapped[str] = mapped_column(String(250), nullable=True)
    has_wifi : Mapped[str] = mapped_column(String(250), nullable=True)
    can_take_calls : Mapped[str] = mapped_column(String(250), nullable=True)
    seats : Mapped[str] = mapped_column(String(250), nullable=True)
    coffee_price  : Mapped[str] = mapped_column(String(250), nullable=True)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

    result = db.session.execute(db.select(Cafe))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_cafes = result.scalars().all()

    print(all_cafes)
 """