from flask import Flask
from flask import render_template

import sqlalchemy as db


list_cafes = []


app = Flask(__name__)


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

#construct table
for r in result:
    list_cafes.append(r._data)
for r in list_cafes:
    print(r)



if __name__  == "__name__":
    app.run(debug =True) 




""" 
@app.route("/")
def home():
    return render_template("index.html")
"""


