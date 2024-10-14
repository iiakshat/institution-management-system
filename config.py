import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ims:ims@localhost/ims'
    SQLALCHEMY_TRACK_MODIFICATIONS = False