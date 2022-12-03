import persona_pb2
from google.protobuf import text_format

FILENAME = ''
person = persona_pb2.persona()
person.local_name = 'who tam i'
person.public_key = b'\x01\x02\x03\x04\x05'

def text_pro():
    text_proto = text_format.MessageToString(person)
    print(text_proto)
    f = open('test.txt','w+')
    f.write(text_proto)
    f.close()

def retrieve_text():
    f = open('test.txt')

text_pro()



