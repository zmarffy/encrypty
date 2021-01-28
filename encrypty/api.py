import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _get_key(key, salt):
    if isinstance(key, str):
        key = key.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(key))
    return key


def generate_salt():
    """Generate a salt for use in encryption

    Returns:
        bytes: The salt
    """
    return os.urandom(16)


def encrypt(data, key, salt):
    """Encrypt an input string or bytes

    Args:
        data (Union[str, bytes]): The data to encrypt
        key (Union[str, bytes]): The key to encrypt the data with
        salt (bytes): The salt

    Returns:
        bytes: The encrypted data
    """
    if isinstance(data, str):
        data = data.encode()
    key = _get_key(key, salt)
    f = Fernet(key)
    out = f.encrypt(data)
    return out


def decrypt(encrypted_data, key, salt):
    """Decrypt an input string or bytes

    Args:
        data (Union[str, bytes]): The data to decrypt
        key (Union[str, bytes]): The key to decrypt the data with
        salt (bytes): The salt

    Returns:
        bytes: The decrypted data
    """
    if isinstance(encrypted_data, str):
        encrypted_data = encrypted_data.encode()
    key = _get_key(key, salt)
    f = Fernet(key)
    out = f.decrypt(encrypted_data)
    return out
