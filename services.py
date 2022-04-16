import dotenv as _dotenv
import jwt as _jwt
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import email_validator as _email_check
import fastapi as _fastapi
import fastapi.security as _security
from sqlalchemy.future import select
import data_base as _database
import schemas as _schemas
import models as _models


_dotenv.load_dotenv()
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
oauth2schema = _security.OAuth2PasswordBearer("/api/token")


async def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


async def get_db():
    db = _database.async_session()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    data = db.execute(select(_models.User).filter(
        _models.User.email == email))

    data = data.scalar_one_or_none()
    return data


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    try:
        valid = _email_check.validate_email(email=user.email)

        email = valid.email
    except _email_check.EmailNotValidError:
        raise _fastapi.HTTPException(
            status_code=404, detail="Please enter a valid email")

    user_obj = _models.User(
        email=email, password_hash=_hash.argon2.hash(user.password))

    db.add(user_obj)
    db.commit()
    await db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(email=email, db=db)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user


def create_token(user: _models.User):
    user_obj = _schemas.User.from_orm(user)

    user_dict = user_obj.dict()
    del user_dict["created_at"]

    token = _jwt.encode(user_dict, SECRET_KEY)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
                            db: _orm.Session = _fastapi.Depends(get_db),
                            token: str = _fastapi.Depends(oauth2schema)):

    try:
        payload = _jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = db.execute(_models.User).get(payload["id"])

    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )
    return _schemas.User.from_orm(user)
