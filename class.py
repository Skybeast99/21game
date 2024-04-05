class Wearpon:
    '''Оружие'''
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f'{self.name} ({self.power})'

class Player:
    def __init__(self, name: str, hp: int, wearpon = None) -> None:
        self.name = name
        self.hp = hp
        self.money = 0
        self.wearpon_default = Wearpon('кулаки', 1)
        if wearpon:
            self.wearpon = wearpon
        else:
            self.wearpon = self.wearpon_default
        self.power = 1
    

    def __str__(self) -> str:
        return f'игрок {self.name}, жизни: {self.hp}, оружие: {self.wearpon}'

    def attack(self, enemy) -> None:
        if self.hp <= 0:
            return 
        damage = self.power + self.wearpon.power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)

class Game:

    def __init__(self) -> None:
        self.player = Player('Вася', 100, Wearpon('Меч', 10))
        self.enemy = Player('упырь', 80)
        self.is_fiting = False
        self.fight()

    def fight(self) -> None:
        self.is_fiting = True
        while self.is_fiting:
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            self.check_winer()
        print('бой окончен')

    def check_winer(self) -> None:
        if self.player.hp <= 0:
            print(self.enemy.name, 'победил')
            self.is_fiting = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'победил')
            self.is_fiting = False
            self.player.money += 10
            print('ваши деньги: ', self.player.money)

Game()