from app import db

class Registration(db.Model):

    __tablename__ = 'registration'

    id =  db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(15), nullable=False)
    
    def __init__(self, userID, email, time, password):
        self.userID = userID
        self.email = email
        self.time = time
        self.password = password
    
    def __repr__(self):
        return "{}{}{}{}{}{}".format(self.id, self.userID, self.email, self.time, self.password)

    
    
class Prediction(db.Model):

    __tablename__ = 'prediction'

    id =  db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(8), nullable=False)
    p_Bee = db.Column(db.Float(10), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, userID, p_Bee, time):
        self.userID = userID
        self.p_Bee = p_Bee
        self.time = time
    
    def __repr__(self):
        return "{}{}{}{}".format(self.id, self.userID, self.p_Bee, self.time)
    

class Collection(db.Model):

    __tablename__ = 'collection'

    id =  db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(8), nullable=False)
    flower = db.Column(db.String(20), nullable=False)
    collectiontype = db.Column(db.String(20), nullable=False)
    
    def __init__(self, userID, flower, collectiontype):
        self.userID = userID
        self.flower = flower
        self.collectiontype = collectiontype
    
    def __repr__(self):
        return "{}{}{}{}".format(self.id, self.userID, self.flower, self.collectiontype)
    
