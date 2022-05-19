import string
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='Password length', type=int, default=0)
parser.add_argument('-t', '--template', help='Enter your template', type=str, default='A2%-%d3%')
parser.add_argument('-f', '--use_digits', help='Indicates the need to use digits', action='store_true', default=True)
parser.add_argument('-c', '--count', help='Amount of symbols', type=int, default=2)
parser.add_argument('-vvv', '--verbose', help='Logging', type=bool, default=False)

args = parser.parse_args()

def parser(param):
    values = ''
    if param == "A":
        values = string.ascii_uppercase
    if param == 'a':
        values = string.ascii_lowercase
    if param == 'd':
        values = string.digits
    if param == 'p':
        values = string.punctuation
    if param == '-':
        values = '-'
    if param == '@':
        values = '@'
    return random.choice(values)

def generate():
    arguments = args.template[:-1].split('%')
    password = ''
    for arg in arguments:
        param = arg[0]
        count =  int(arg[1:]) if len(arg) > 1 else 1
        for i in range(count):
            password += parser(param)
    return password

def genereteRandom():
    valid_symbols = 'Aadp-@';
    password = ''
    for i in range(args.length):
        param = random.choice(valid_symbols)
        password += parser(param)
    return password

def numberOfPasswords():
    passwords = []
    for i in range(args.count):
        if args.length:
            passwords.append(genereteRandom())
        else: passwords.append(generate())
    return passwords

generated_passwords = []
if(args.count):
    generated_passwords = numberOfPasswords();
else:
    generated_passwords = genereteRandom()

print(generated_passwords)