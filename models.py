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

# class Post(_database.Base):
#     __tablename__ = "posts"
#     id = _sql.Column(_sql.Integer, primary_key=True, index=True)
#     owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
#     post_text = _sql.Column(_sql.String, index=True)
#     date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

#     owner = _orm.relationship("User", back_populates="posts")