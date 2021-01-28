import argparse
from . import api
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["encrypt", "decrypt"])
    parser.add_argument("file")
    parser.add_argument("key")
    parser.add_argument("salt", nargs="?")
    args = parser.parse_args()

    salt_generated = False

    if args.action == "encrypt":
        if args.salt is None:
            salt_generated = True
            args.salt = api.generate_salt()
            print(f"Salt is: {args.salt}")
        func = api.encrypt
    else:
        if args.salt is None:
            parser.error("Must provide salt when decrypting")
        func = api.decrypt

    if not salt_generated:
        with open(args.salt, "rb") as f:
            args.salt = f.read()

    with open(args.file, "rb") as f:
        data = f.read()
    with open(args.key, "rb") as f:
        args.key = f.read()

    d = func(data, args.key, args.salt)
    with open(args.file, "wb") as f:
        f.write(d)


if __name__ == "__main__":
    sys.exit(main())
