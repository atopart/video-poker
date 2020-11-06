import random
import time

def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck

def choix_cartes(tirage):
    jeu = []
    for i in tirage:
        print(i)
        choix = input('Conserver cette carte ? y/n :')
        if choix == 'y':
            jeu.append(i)
    return jeu

def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    carte_a_tirer = 5 - nb_carte
    nouvelle_carte = random.sample(deck, carte_a_tirer)
    for i in nouvelle_carte:
        jeu.append(i)
    return jeu

def machine():
    #deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    deck = ['2-♥', '3-♥', '4-♥', '5-♥', '6-♥', '7-♥', '8-♥', '9-♥', '10-♥', 'J-♥', 'Q-♥', 'K-♥', 'A-♥', '2-♦', '3-♦',
            '4-♦', '5-♦', '6-♦', '7-♦', '8-♦', '9-♦', '10-♦', 'J-♦', 'Q-♦', 'K-♦', 'A-♦', '2-♣', '3-♣', '4-♣', '5-♣',
            '6-♣', '7-♣', '8-♣', '9-♣', '10-♣', 'J-♣', 'Q-♣', 'K-♣', 'A-♣', '2-♠', '3-♠', '4-♠', '5-♠', '6-♠', '7-♠',
            '8-♠', '9-♠', '10-♠', 'J-♠', 'Q-♠', 'K-♠', 'A-♠']
    tirage1, deck = premier_tirage(deck)
    print('Premier Tirage : \n')
    time.sleep(1)
    print(tirage1)
    print('\n')
    jeu = choix_cartes(tirage1)
    tirage_final = deuxieme_tirage(jeu, deck)
    print('Deuxième Tirage: \n')
    time.sleep(1)
    print (tirage_final)
    print('\n')
    return tirage_final