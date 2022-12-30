from pydantic import BaseModel


class UserBase(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    email: str
    number: int | None = "Invalid"
    birth_date: str


class TeamBase(BaseModel):
    id: int | None = None
    team_name: str
    captain_team: str
    played_games: int
    ranking: int


class StadiumBase(BaseModel):
    id: int | None = None
    stadium_name: str
    city: str
    capacity: float
    age: int


class TeamCreate(TeamBase):
    pass


class UserCreate(UserBase):
    password: str


class StadiumCreate(StadiumBase):
    pass


class Team(TeamBase):
    class Config:
        orm_mode = True


class User(UserBase):
    class Config:
        orm_mode = True


class Stadium(StadiumBase):
    class Config:
        orm_mode = True
