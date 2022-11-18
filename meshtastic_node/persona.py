import persona_pb2
from google.protobuf import text_format
import os


class Persona:

    """ The Persona conatins a key pair and it's relationships to other keys.
        'Owned' personas will have one or more secret keys.
    """
    
    def __init__(self, local_name, mac_address):
        """ Each new Persona represents a single 'owned' key pair. The Persona
            serves as a handle for all cryptographic secrets and state supported
            by the cipher suite.
        """
        self.person = persona_pb2.persona() # wrapping the protobuf class to hold values
        self.person.local_name = local_name
        self.person.mac_address = mac_address
        self.peers = {}   # peers indexed by public key
    
    def save_keys(self, pkey, skey):
        """ Save a persona's public and private keys its protobuf
        """
        print("saving key to protobuf")

        self.person.public_key = pkey
        self.person.private_key = skey

    def write_all_secrets_to_file(self):
        path_to_script = os.path.dirname(os.path.abspath(__file__))
        fileName = os.path.join(path_to_script, "config.txt")
        f = open(fileName,'ab')
        #f.write(text_proto)
        f.write(self.person.SerializeToString())
        f.close()

    def get_pkey(self):
        return self.person.public_key

    def get_skey(self):
        return self.person.private_key
    


mike = Persona("12220 Dalian","Ahabi")
mike.write_all_secrets_to_file() 
# print(mike.person.SerializeToString())

