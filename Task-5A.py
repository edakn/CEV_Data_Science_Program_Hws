# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import psycopg2
import time
import random
import pandas as pd

fake_info=Faker()

engine = create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
dbConnection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

session = sessionmaker(bind = engine)()

class Login(Base):
  __tablename__ = "Login"
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key = True)
  email = Column(String(50))
  password = Column(String(50))


class Finds(Base):
    __tablename__ = 'Findings'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    email = Column(String(50))
    password = Column(String(50))

start_time = time.time()    
Base.metadata.create_all(engine)
session.commit()

def fake_info_generator(i):
  info = []
  for i in range(i):
   rows=[]
   rows.append(fake_info.email())
   rows.append(fake_info.password())
   info.append(rows)
  return info

df = pd.DataFrame(fake_info_generator(10000), columns=["email", "password"])


df.to_sql('Login', engine, if_exists='replace')
query1 = pd.read_sql("select * from \"Login\" order by random() LIMIT 1000", dbConnection).drop(['index'],axis=1)
query2 = pd.read_sql("select * from \"Login\"", dbConnection).drop(['index'] , axis=1)

query1 = query1.append(pd.DataFrame(fake_info_generator(10000), columns=["email", "password"]),ignore_index=True)
pd.merge(query1,query2,'inner',['email','password']).to_sql('Findings', engine, if_exists='replace')
print(time.time()-start_time)