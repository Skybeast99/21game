from random import shuffle
from os import system

def get_deck() -> list[dict]:
    suits = ('пик', 'крести', 'буби', 'черви')
    cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'валет': 10,
    'дама': 10,
    'король': 10,
    'туз': 11
    }

    deck = []

    for suit in suits:
        for item in cards:
            card = {
                'цена': cards[item],
                'масть': suit,
                'название': item,
            }
            deck.append(card)
    return deck


def get_players() -> list[dict]:
    '''возращает список играков'''
    player_1 = {
        'имя': 'вася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }

    player_2 = {
        'имя': 'ася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    '''раздает каждому игроку карты'''
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop())


def show_cards() -> None:
    for card in player['карты']:
        print(card['название'], card['масть'])


deck = get_deck()
shuffle(deck)
players = get_players()
deal_cards(2)


if players[0]['карты'][1] in deck:
    print('!!!!!')

for player in players:
    while True:
        system('cls')
        show_cards()
        player_option = input('взять карту из колоды (y/n)? ')
        if player_option.lower() == 'y':
            player['карты'].append(deck.pop())   
        elif player_option.lower() == 'n':
            break
        else:
            print('у вас опечатка')

for player in players:
    for card in player['карты']:
        player['сумма'] += card['цена']
    print(player['имя'], player['сумма'])

print()