from machine import machine
from gain import gain

bankroll = int(input("Combien d'argent mettez vous : "))
mise_joueur = int(input("Votre mise : "))

def partie(mise, bankroll):
    main = machine()
    g, resultat = gain(main, mise)
    bankroll = bankroll - mise
    bankroll += g
    return resultat, bankroll

while bankroll - mise_joueur >= 0:
    resultat, bankroll = partie(mise_joueur, bankroll)
    print(resultat)
    print("Argent restant : " + str(bankroll))
    if bankroll == 0:
        print("Vous n'avez plus d'argent, au revoir.")
        break
    else:
        mise_joueur = int(input("Votre mise : "))
        if bankroll - mise_joueur <0:
            print("Vous n'avez pas assez d'argent !")
            mise_joueur = int(input("Votre mise : "))