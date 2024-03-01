from random import shuffle

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
            'цена' : cards[item],
            'масть' : suit,
            'название' : item,
        }
        deck.append(card)

shuffle(deck)

player_1 = {
    'имя': 'вася',
    'карты': [],
    'человек': True
}

player_2 = {
    'имя': 'вася',
    'карты': [],
    'человек': True
}

players = (player_1, player_2)

for player in players:
    for i in range(2):
        player['карты'].append(deck.pop())

for player in players:
    print(player['карты'])

print('число карт в колоде: ', len(deck))

for card in deck:
    print(card)
    print('-' * 50)
