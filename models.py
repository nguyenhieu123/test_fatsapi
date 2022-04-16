import datetime as _dt
import sqlalchemy as _sql
import passlib.hash as _hash
import data_base as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password_hash = _sql.Column(_sql.String)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    def verify_password(self, password):
        return _hash.argon2.verify(password, self.password_hash)
