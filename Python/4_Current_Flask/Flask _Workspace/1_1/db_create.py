from app import db
from models import BlogPost


db.create_all() 
 
db.session.add(BlogPost("HIO","bPK"))
db.session.commit()


 