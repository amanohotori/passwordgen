import argparse
import os
import datetime
import string
import secrets

def get_current_date_string():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")

def save_to_file(directory, filename, text):
    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write(text)
    print(f'Saved to file: {filepath}')

def get_filename(args):
    current_date = get_current_date_string()
    filename = f"password_strings_{'sign' if args.nosign else 'nosign'}_{args.pwdlength}_{current_date}.txt"
    return filename

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--pwdlength", help="Generating password length. (Integral value)",
                    type=int, default=64, metavar=NotImplemented)
parser.add_argument("-s", "--nosign", help="Without sign option.",
                    action="store_false")
args = parser.parse_args()

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
signs = "/-+.!#$%,_@"

charset = lowercase + uppercase + digits
if args.nosign:
    charset = charset + signs

chars = [secrets.choice(charset) for _ in range(args.pwdlength)]
pwdstring = ''.join(chars)

print(pwdstring)

user_choice = input("Do you want to save the password string to a file? (Y/N): ")
if user_choice.lower() == 'y':
    directory = input("Enter a directory path (leave empty for default path): ")
    if directory == "":
        # default path is set to the current directory
        directory = os.getcwd()
    directory = os.path.join(directory, "pwdstrings")
    filename = get_filename(args)
    save_to_file(directory, filename, pwdstring)