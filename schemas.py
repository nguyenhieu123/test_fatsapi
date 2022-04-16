import datetime as _dt

import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int
    created_at: _dt.datetime

    class Config:
        orm_mode = True


class UserLogin(_UserBase):
    password: str
