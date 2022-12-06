from black_lager import persona_pb2
import sys


def read_wallet_from_file(wallet_message):
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "WALLET_FILE")
        sys.exit(-1)

    try:
        f = open(sys.argv[1], "rb")
        wallet_message.ParseFromString(f.read())
        f.close()
    except IOError:
        print(sys.argv[1] + ": Could not open file.  Creating a new one.")


def get_persona_input(persona):
    persona.local_name = input("Enter name: ")
    persona.owned = True

    return persona


def write_wallet_to_file(wallet):
    # serializes the message and returns it as a string.
    # Note that the bytes are binary, not text; we only use the str type as a convenient container.
    wallet.SerializeToString()
    f = open(sys.argv[1], "wb")
    f.write(wallet.SerializeToString())
    f.close()


wallet = persona_pb2.Wallet()
read_wallet_from_file(wallet)
new_persona = wallet.my_personas.add()
get_persona_input(new_persona)
print(wallet)
write_wallet_to_file(wallet)
