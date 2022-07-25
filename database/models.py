from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Social(Base):
    __tablename__ = 't_social'
    id = Column(Integer, primary_key=True, autoincrement=True)
    social_media = Column(String)


class Account(Base):
    __tablename__ = 't_account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    social_id = Column(Integer, ForeignKey('t_social.id'))


class ProfilesFacebook(Base):
    __tablename__ = 't_profiles_instagram'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)


class ProfilesInstagram(Base):
    __tablename__ = 't_profiles_facebook'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
