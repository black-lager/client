from cipher_suite.nacl_suite import naclSuite
import sys
import nacl.utils
from nacl.public import PrivateKey, Box
from nacl.signing import SigningKey
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder

# Return public key and private key
def generate_key():
    test_suite = naclSuite()
    return test_suite.generate_key_pairs('testing')

# Test size of public and private key
def test_answer():
    public, private = generate_key()
    assert sys.getsizeof(public)== 32 and sys.getsizeof(private) == 32

# Test encryption / decryption message using nacl box
def decrypt():
    skbob = PrivateKey.generate()
    pkbob = skbob.public_key
    skalice = PrivateKey.generate()
    pkalice = skalice.public_key

    bob_box = Box(skbob, pkalice)
    message = b"Testings"
    encrypted = bob_box.encrypt(message)
    alice_box = Box(skalice, pkbob)

    plaintext = alice_box.decrypt(encrypted)
    assert str(message) == str(plaintext.decode('utf-8'))

# Test for forged signature
def real_signature():
    signing_key = SigningKey.generate()

    signed = signing_key.sign(b"Testings")

    verify_key = signing_key.verify_key

    verify_key_bytes = verify_key.encode()
    verify_key = VerifyKey(verify_key_bytes)

    try:
        verify_key.verify(signed.message, signed.signature)
    except nacl.exceptions.BadSignatureError:
        print("nacl.exceptions.BadSignatureError: Signature was forged or corrupt")

def forged_signature():
    signing_key = SigningKey.generate()

    signed = signing_key.sign(b"Testings")

    verify_key = signing_key.verify_key

    verify_key_bytes = verify_key.encode()
    verify_key = VerifyKey(verify_key_bytes)

    forged = signed[:-1] + bytes([int(signed[-1]) ^ 1])
    try:
        verify_key.verify(forged)
    except nacl.exceptions.BadSignatureError:
        print("nacl.exceptions.BadSignatureError: Signature was forged or corrupt")
        

# Test hex encoder
def hex_encoder():
    signing_key = SigningKey.generate()

    signed_hex = signing_key.sign(b"Testing", encoder=HexEncoder)
    verify_key = signing_key.verify_key

    verify_key_hex = verify_key.encode(encoder=HexEncoder)

    verify_key = VerifyKey(verify_key_hex, encoder=HexEncoder)

    signature_bytes = HexEncoder.decode(signed_hex.signature)
    verify_key.verify(signed_hex.message, signature_bytes,
                encoder=HexEncoder)


    forged = signed_hex[:-1] + bytes([int(signed_hex[-1]) ^ 1])
    verify_key.verify(forged)