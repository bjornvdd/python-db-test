from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import authorization
from fastapi.middleware.cors import CORSMiddleware
import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()

# implementing security
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://bjornvdd.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = authorization.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = authorization.create_access_token(
        data={"sub": user.email}
    )
    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/make/player", response_model=schemas.User)
async def create_player(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post("/make/team", response_model=schemas.Team)
async def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)


@app.post("/make/stadium", response_model=schemas.Stadium)
async def create_stadium(stadium: schemas.StadiumCreate, db: Session = Depends(get_db)):
    return crud.create_stadium(db=db, stadium=stadium)


@app.get("/all/players", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/all/teams", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams


@app.get("/all/stadiums", response_model=list[schemas.Stadium])
def read_stadiums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    stadiums = crud.get_stadiums(db, skip=skip, limit=limit)
    return stadiums


@app.get("/team/rank")
def team_rank(rank: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    teams = crud.get_rank(db, rank=rank)
    if teams is None:
        raise HTTPException(status_code=404, detail="Rank not found, please try again!")
    return teams


@app.delete("/remove/player")
def remove_player(last_name: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.remove_player(db, last_name=last_name)
    return db_user


@app.put("/change/player")
def change_player(player_id: int, user: schemas.UserCreate, db: Session = Depends(get_db),
                  token: str = Depends(oauth2_scheme)):
    db_user = crud.change_player(db, player_id=player_id, user=user)
    return db_user


@app.put("/change/captain")
def change_captain(team_id: int, team: schemas.TeamCreate, db: Session = Depends(get_db),
                   token: str = Depends(oauth2_scheme)):
    db_user = crud.change_captain(db, team_id=team_id, team=team)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Captain not found, please try again!")
    return db_user
