import random

nbr_secret = random.randint(1,100)
invite = 'Propose un nombre : '

while True:
    nbr_joueur = input(invite)
    if nbr_secret == int(nbr_joueur):
        print('Correct!')
        break
    elif nbr_secret > int(nbr_joueur):
        print('Trop bas')
    else:
        print('Trop haut')
