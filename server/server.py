
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import base
import socket
from packet import packet
import pickle
import user

engine = create_engine('sqlite:///Data.db')
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)

openConnection = True
#Initialize the database, and create an engine and session for SQLAlchemy

def main():
        """The main function will handle the network connections, and
	will send incoming packets where they need to go.
	
	Main also sets up the server's public and private keys if they don't already exist.
	If they do exist, they will be pulled from a file and stored in RAM.
        """

        HOST = '127.0.0.1'
        PORT = 20987


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        while True:
            conn, addr = s.accept()
            data = conn.recv(4096)
            if not data:
                break
            clientData = pickle.loads(data)
            print(clientData.user)
            print(clientData.salt)
            print(clientData.password)
            print(clientData.key)

            if(clientData.command == 1):
                newUser(clientData)
            elif(clientData.command == 2):
                login(clientData)
            elif(clientData.command == 3):
                sendReceive(clientData)

        s.close()
def newUser(packet):
        """newUser will handle the creation of new accounts in the database.
        """
        session = Session()
        newUser = user.User(packet.user, packet.salt, packet.password, packet.key)
        session.add(newUser)
        session.commit()
        openConnection = False
def login(packet):
        """login handles all login attempts
        """

def sendReceive(packet):
        """sendReceive updates the server and user's mail databases.
        """
main()
