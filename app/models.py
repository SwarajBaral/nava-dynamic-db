from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey

Base = declarative_base()

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    db_name = Column(String, unique=True, nullable=False)
    db_user = Column(String, nullable=False)
    db_password = Column(String, nullable=False)  # TODO: Should be hashed
    created_at = Column(TIMESTAMP, server_default=func.now())

class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey("organizations.id", ondelete="CASCADE"))
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)