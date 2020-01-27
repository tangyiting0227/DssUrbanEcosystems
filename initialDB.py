from app import db
from models import Registration, Prediction, Collection
from datetime import datetime
import os

db.drop_all()
db.create_all()

db.session.add(Registration("admin", "admin@citybuzz.com", datetime.now(), "administration")) #save
db.session.commit() # confirm