# `encrypty`

`encrypty` is a simple Python library for encrypting and decrypting stuff. It was inspired by [simple-crypt](https://github.com/andrewcooke/simple-crypt).

## Usage
Use the public functions to generate a salt for encryption, encrypt, and decrypt stuff.

```python
from getpass import getpass

from encrypty import generate_salt, encrypt, decrypt

salt = generate_salt()
password = getpass("Enter a password: ")
secret_string = "secret message lol"

encrypted_bytes = encrypt(secret_string, password, salt)

decrypted_bytes = decrypt(encrypted_bytes, password, salt)
decrypted_string = decrypted_bytes.decode()

print(decrypted_string)  # secret message lol
```

This works with a bytes or string key and bytes or string data to encrypt.
