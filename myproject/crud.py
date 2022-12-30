from sqlalchemy.orm import Session

import models
import schemas
import authorization


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()


def get_stadiums(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stadium).offset(skip).limit(limit).all()


def get_rank(db: Session, rank: str):
    team = db.query(models.Team).filter(models.Team.ranking == rank).first()
    return team


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = authorization.get_password_hash(user.password)
    db_user = models.User(first_name=user.first_name, last_name=user.last_name, email=user.email, number=user.number,
                          birth_date=user.birth_date, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(team_name=team.team_name, captain_team=team.captain_team, played_games=team.played_games,
                          ranking=team.ranking)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def create_stadium(db: Session, stadium: schemas.StadiumCreate):
    db_stadium = models.Stadium(stadium_name=stadium.stadium_name, city=stadium.city, capacity=stadium.capacity,
                                age=stadium.age)
    db.add(db_stadium)
    db.commit()
    db.refresh(db_stadium)
    return db_stadium


def remove_player(db: Session, last_name: str):
    db_user = db.query(models.User).filter(models.User.last_name == last_name).first()
    db.delete(db_user)
    db.commit()
    return db_user


def change_player(db: Session, player_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == player_id).first()
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db_user.number = user.number
    db_user.birth_date = user.birth_date
    db_user.password = authorization.get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user


def change_captain(db: Session, team_id: int, team: schemas.TeamCreate):
    db_user = db.query(models.Team).filter(models.Team.id == team_id).first()
    db_user.captain_team = team.captain_team
    db.commit()
    db.refresh(db_user)
    return db_user


