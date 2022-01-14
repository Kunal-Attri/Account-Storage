import random
import time
from os import path

if not path.exists('pass.txt'):
    file = open("pass.txt", 'w')
    file.write('pqrstefghiijklmopqr')
    file.close()
file = open("pass.txt", "r")
pw = file.read()
file.close()
prev_password = ""
encryptor = ['##9p', 'JHGF', '65=P', '?o7&', '$H%N', '~KBC', 'iRM0', '8888', '@9NH', 'tT*y', 'el?N', '1221', '?Fg%',
             'GHJB', 'kJnH', '6/kU', '9sTc', 'q3D2', 'f1!%', 'b7{5', 'K}A9', 'Nr8Y', 'XPjy', '64@5', 'OoP0', 'Q.k:',
             'Tu5*', '"ty/', 'I#5-', '@jun', 'time', 'may$', 'logs', 'fix%', 'moon', '3sun', 'funL', 'leg0', 'po*n',
             '*u*k', 'die2', 'Ucry', 'iLIE', '2day', 'hWRu', '4JEE', 'IIIT', 'nSiT', 'nSuT', '+day', 'Wlcm',
             '=hi*', 'mrs.', 'srie', '(is)']

for i in range(4, len(pw), 5):
    prev_password += pw[i]
attempts = 5


def reg_new_password():
    new_password = ""
    new_pass = input("Enter new password: ")
    for i in range(len(new_pass)):
        encrypt = random.randint(0, 51)
        new_password += encryptor[encrypt] + new_pass[i]
    new_password += encryptor[random.randint(0, 54)]
    fil = open('pass.txt', 'w')
    fil.write(new_password)
    fil.close()
    print('New password set')
    time.sleep(3)


while attempts > 0:
    usr_prv_pw = input("Enter previous password: ")
    if usr_prv_pw == prev_password:
        reg_new_password()
        break
    else:
        attempts -= 1
        print(f"Wrong password entered. Attempts left: {attempts}")
else:
    print("You have gone out of all your attempts available")
    time.sleep(3)
