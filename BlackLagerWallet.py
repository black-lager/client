from black_lager import persona_pb2
import sys


class BlackLagerWallet:
    def __init__(self):
        """Initialize a Wallet object. Check if a command line argument is provided for the wallet file.
        If there is one provided, then set it as the wallet path. Else set the default wallet path
        """
        self.wallet_message = persona_pb2.Wallet()

        if len(sys.argv) == 1:
            self.wallet_path = "./wallet"
        elif len(sys.argv) == 2:
            self.wallet_path = sys.argv[1]
        else:
            print("Usage:", sys.argv[0], "WALLET_FILE")
            sys.exit(-1)

    def read_wallet_from_file(self):
        """Read wallet data from the wallet_path file and parse it into the wallet_message protobuf object"""
        try:
            f = open(self.wallet_path, "rb")
            self.wallet_message.ParseFromString(f.read())
            f.close()
        except IOError:
            print("Could not open wallet file. Creating a new one.")

    def create_new_persona(self):
        """Add a new owned persona to the wallet and prompt the user for its data"""
        new_persona = self.wallet_message.my_personas.add()
        new_persona.local_name = input("Enter name: ")
        new_persona.owned = True

    def write_wallet_to_file(self):
        """Writes wallet data out to a file on disk"""
        # serializes the message and returns it as a string.
        # Note that the bytes are binary, not text; we only use the str type as a convenient container.
        f = open(self.wallet_path, "wb")
        f.write(self.wallet_message.SerializeToString())
        f.close()


wallet = BlackLagerWallet()
wallet.read_wallet_from_file()
wallet.create_new_persona()
print(wallet.wallet_message)
wallet.write_wallet_to_file()
