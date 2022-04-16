import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas
from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware

app = _fastapi.FastAPI()
app.add_middleware(PyInstrumentProfilerMiddleware)


@app.post("/api/users")
async def create_user(
                    user: _schemas.UserCreate,
                    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    # db_user = _services.get_user_by_email(email=user.email, db=db)
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400,
            detail="User with that email already exists")
    # user = _services.create_user(user=user, db=db)
    user = await _services.create_user(user=user, db=db)
    # return _services.create_token(user=user)
    return _services.create_token(user=user)


@app.post("/api/token")
async def generate_token(
                        form_data: _schemas.UserLogin,
                        db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.authenticate_user(
        email=form_data.email, password=form_data.password, db=db)

    if not user:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Credentials")

    return _services.create_token(user=user)


@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(
                     user: _schemas.User = _fastapi.Depends(
                         _services.get_current_user)):
    return user
