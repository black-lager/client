import nacl.utils
from meshtastic_node import persona_pb2
from nacl.public import PrivateKey, Box
import os, sys

class naclSuite():
    # suite for PyNaCl

    def __init__(self):
        # Secret vault stores collections of device name & corresponding keys
        self.secret_vault = {}
        self.book = persona_pb2.secret_book()

    def align_with_config(self):
        people = self.read_from_config()
        for person in people:
            self.secret_vault[person.local_name] = (person.public_key, person.private_key)
    
    def get_config_path(self):
        path_to_script = os.path.dirname(os.path.realpath(__file__))
        return path_to_script[:-13] + "/meshtastic_node/config.txt"

    def read_from_config(self):
        fileName = self.get_config_path()
        temp = persona_pb2.secret_book()
        f = open(fileName, "rb")
        temp.ParseFromString(f.read())
        print( type(temp.person))
        for person in temp.person:
            print (person.local_name)
            print (person.public_key)
            print (person.private_key)

    # Public / private key generator using Curve25519
    # Uses device_name as key
    def generate_key_pairs(self,device_name: str):
        # Keys are 48 bytes

        newPrivateKey = PrivateKey.generate()
        newPublicKey = newPrivateKey.public_key
        try:
            self.secret_vault[device_name] = [newPublicKey,newPrivateKey]
            print("keys generation succeed")
        except AttributeError:
            print("attribute error, secret vault most likely not initialized")
            return
            
        return newPublicKey, newPrivateKey
    
    # Remove a device key pairs using device_name
    def remove_key_pairs(self, device_name: str):
        try:
            del self.secret_vault[device_name]
            print("Successfully deleted key")
        except Exception as e:
            print(repr(e))
    
    # Print out all device names and key pairs
    def fbi_open_up(self):
        for eachKey in self.secret_vault.keys():
            print("Device name : " + eachKey)
            print("Public Key:")
            print(self.secret_vault[eachKey][0])
            print("Private Key: ")
            print(self.secret_vault[eachKey[1]])
        
    def add_person_to_book(self, localName, address, num, public_key=b'0', private_key=b'0'):
        new_dude = persona_pb2.persona()
        new_dude.local_name = localName
        new_dude.mac_address = address
        new_dude.node_num = num
        new_dude.public_key = bytes(public_key)
        new_dude.private_key = bytes(private_key)
        self.book.person.append(new_dude)

    def write_all_secrets_to_file(self):
        fileName = self.get_config_path()
        f = open(fileName,'ab')
        f.write(self.book.SerializeToString())
        f.close()

    def print_book(self):
        print(self.book)
