from sqlalchemy import Column, Integer, String, Float
from database import Base


class User(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    number = Column(Integer, unique=True, index=True)
    birth_date = Column(String)
    password = Column(String)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)

    team_name = Column(String)
    captain_team = Column(String)
    played_games = Column(Integer)
    ranking = Column(Integer, unique=True, index=True)




class Stadium(Base):
    __tablename__ = "stadiums"

    id = Column(Integer, primary_key=True, index=True)
    stadium_name = Column(String, unique=True, index=True)
    city = Column(String)
    capacity = Column(Float)
    age = Column(Integer)



