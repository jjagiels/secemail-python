
import sqlite3
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class User(Base):
    __tablename__ = 'user'

    pid = Column(Integer, primary_key=True)
    alias = Column(String)
    salt = Column(String)
    password = Column(String)
    key = Column(String)


    def __init__(self, alias, salt,  password, key):
        """The standard constructor will create a user with the supplied
		information from the deserialized TCP stream.

        @args
		alias: The alias that the users wishes to use on this server
		
		password: The *HASHED* password the user chose
		
		key: The user's public key
		
        """
        self.alias = alias
        self.salt = salt
        self.password = password
        self.key = key
