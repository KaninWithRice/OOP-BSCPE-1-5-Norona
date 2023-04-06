# Mohammad Mishal S. Noroña | BSCPE 1-5 | PROBLEM 2 – DECRYPTION
# add Color to the program
import colorama
from colorama import Fore, Back, Style
colorama.init()
# add introduction
print("")
print(Fore.LIGHTYELLOW_EX + "WELCOME TO THE PROGRAM".center(40," ") )
print(Fore.LIGHTYELLOW_EX + "By: Mishal Noroña".center(40," ") )
# ask user for input
letter_input = input(Fore.CYAN + "Enter the text you want to decrypt:")
letter_output = ""
# check each character
for x in range(len(letter_input)):
# if *, change to a
    if letter_input[x] == "*":
        letter_output += "a"
# if &, change to e
    elif letter_input[x] == "&":
        letter_output += "e"
# if #, change to i
    elif letter_input[x] == "#":
        letter_output += "i" 
# if +, change to o
    elif letter_input[x] == "+":
        letter_output += "o"
# if !, change to u
    elif letter_input[x] == "!":
        letter_output += "u"
    else:
        letter_output += letter_input[x]

# add loading time
import time
import sys

done = 'false'
# add animation
def animation():
        sys.stdout.write(Fore.RED + '\n\rDecrypting Please Wait ▒▒▒▒▒▒▒▒▒▒  0%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait █▒▒▒▒▒▒▒▒▒  10%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ██▒▒▒▒▒▒▒▒  20%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ███▒▒▒▒▒▒▒  30%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ████▒▒▒▒▒▒  40%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait █████▒▒▒▒▒  50%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ██████▒▒▒▒  60%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ███████▒▒▒  70%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ████████▒▒  80%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait █████████▒  90%')
        time.sleep(0.5)
        sys.stdout.write(Fore.RED + '\rDecrypting Please Wait ██████████ 100%')
        time.sleep(0.3)
        sys.stdout.write(Fore.LIGHTGREEN_EX +'\n\nDECRYPTION COMPLETE\n')

animation()
# print output
print (Fore.LIGHTMAGENTA_EX + Style.BRIGHT + Back.LIGHTWHITE_EX + letter_output)