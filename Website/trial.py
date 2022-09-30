# import numpy as np
# import matplotlib.pyplot as plt
import server 
from sqlalchemy.orm import sessionmaker
import random 

#SQLLite


# c.execute(""" CREATE TABLE user (
#     name text,
#     distance integer) """)
# c.execute("INSERT INTO user VALUES ('Magdy','1234')")
# c.execute("SELECT * FROM user")
# print(c.fetchall())
# conn.commit()
# #close
# conn.close()

# #new session
# Session = sessionmaker(bind=server.engine)
# session = Session()

# # adding random data
# for t in range (10,20):
#     item_id = random.randint(0,1000)
#     price = random.randint(20,50)

#     tr = server. transactions(t, '2020/05/06', item_id, price)
#     session.add(tr)

# # save changes in data base
# session.commit()

# SQLLite (Failed)
# #connect with data
# engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
# #manage tables
# base = declarative_base()

# class transactions (base):

#     __tablename__ = 'transactions'

#     transactions_id = Column(Integer, primary_key = True)
#     date = Column(String)
#     item_id = Column(Integer)
#     price = Column(Integer)

#     def __init__(self, transaction_id, date, item_id, price):
#         self.transactions_id = transaction_id
#         self.date = date
#         self.item_id = item_id
#         self.price = price

# base.metadata.create_all(engine)

# SQL Alchemy (Failed)
# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///space.db'
# # initilaize database
# db = SQLAlchemy(app)

# #Create database model
# class Space(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False )
#     #Create a function to return string 
#     def __repr__(self):
#         return '<Name %>' % self.id


# ------------------------------------------------
# hazards = [0.2,0.4,0.6,0.8]
# organismsForGravity = {
#     'human': 4.8*hazards[0],
#     'mice': 4*hazards[0],
#     'rat': 3.5*hazards[0]
# }
# organismsForRadiation = {
#     'dr': 2.4*hazards[1],
#     'tard':2.1*hazards[1],
#     'human':1.85*hazards[1]
# }
# organismsForDna = {
#     'tard' : 1.55 * hazards[2],
#     'nmr': 1.3* hazards[2],
#     'mice':1.1* hazards[2]
# }
# organismsForeye = {
#     'rbs': 1.2* hazards[3],
#     'human':1* hazards[3],
#     'eagle':0.8* hazards[3]
# }
# probabilities  = []
# for keyG,valG in organismsForGravity.items():
#     for keyR,valR in organismsForRadiation.items():
#         for keyD,valD in organismsForDna.items():
#             for keyE,valE in organismsForeye.items():
#                 probabilities.append(valG * valR * valD * valE)
                
                
# print(probabilities)
# plt.hist(probabilities)
# plt.show()