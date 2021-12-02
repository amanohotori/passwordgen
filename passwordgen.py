import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--pwdlength", help="Generating password length. (Integral value)",
                    type=int, default=64, metavar=NotImplemented)
parser.add_argument("-s", "--nosign", help="Without sign option.",
                    action="store_false")
args = parser.parse_args()

import string
import secrets

chars = []

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
signs = "/-+.!#$%,_@"

charset = lowercase + uppercase + digits

if args.nosign:
    charset = charset + signs

while len(chars) <= args.pwdlength:
    chars.append(secrets.choice(charset))
else:
    pwdstring = ''.join(chars)
    print(pwdstring)