import socket
from packet import packet
import pickle
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
import hashlib

HOST = '127.0.0.1'
PORT = 20987

def main():
    """The main function will handle the network connections, and
    will send outgoing packets to the server.
    
    Main also shows the UI prompts and messages
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    newUser(s)
    """    
    print("1: Create an Account\n2: Login\n")
    userInput = input("Select an option: ")
    if(userInput == "1"):
        print("Hello, world!")
    elif(userInput == "2"):
        print("Goodbye, world!")
    else:
        print("Broken")
    """
def newUser(socket):
    """newUser will handle the creation of new accounts in the database.
    """
    #ask user for input regarding username and password, hash the password, generate public and private keys, then create
    # a packet object, pickle it (serialize it) and send it to the server
    
    #Generate the private key
    privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
            )
    #extract the public key from the private key object
    publicKey = privateKey.public_key()

    #serialize and store the private key
    pem = privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
            )
    with open('private_key.pem', 'wb') as f:
        f.write(pem)

    #serialize and store the public key
    pem = publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)

    #Generate a salt of 64 bytes for the password from the os's crypto-random store
    salt = os.urandom(64)

    #**TEMP PASSWORD**
    password = b'badpassword'

    #hash the password using the user's input and the generated salt
    hashBrown = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

    testPacket = packet()
    testPacket.prepNewUser("justin", salt, hashBrown, pem)
    print("User sent to server.")
    testPacket.command = 1
    data = pickle.dumps(testPacket)
    print(data)
    socket.send(data)
    #data = socket.recv(1024)
    #print('received', repr(data))
        
def login(socket):
    """login handles all login attempts
    """
    #Once user has entered thier information, the flow of data transfers will be:
    #Client sends username to server and requests that user's salt -> 
    #If that user doesn't exist, return an error and have the user enter thier information again ELSE ->
    #Return that user's salt to the client ->
    #Hash the password with the salt ->
    #Send the hashed password to the server ->
    #Server compares the two hashes, if they are the same, return a success and advance the client to the next window ELSE ->
    #If the hashes differ, then return an error and have the user enter thier information again

def sendReceive(socket):
    """sendReceive updates the server and user's mail databases.
    """
main()
