import os


class Wearpon:
    '''Оружие'''
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f'{self.name} ({self.power})'


class Player:
    def __init__(self, name: str, hp: int, weapon=None, power=1, xp=0, level=1) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.level = level
        self.xp = xp
        self.money = 0
        self.weapon_default = Wearpon('кулаки', 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.weapon_default
    
    def show(self) -> None:
        print(self.name.center(20, '-'))
        print('жизни:', self.hp)
        print('сила:', self.power)
        print('деньги:', self.money)
        print('опыт:', self.xp)
        print('левел:', self.level)
        print('оружие : ', self.weapon)

    def attack(self, enemy) -> None:
        if self.hp <= 0:
            return 
        damage = self.power + self.weapon.power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)

    def get_award(self, enemy) -> None:
        self.xp += enemy.level
        while self.xp > self.level * 10:
            self.level += 1
        self.money += 10
        print('~~~~~~~~~~~~~~~~~~~~')
        print(self.name, 'получил', enemy.level, 'опыта')
        self.show()
        print('ваши деньги: ', self.money)
        print(self.level)
    

class Game:

    def __init__(self) -> None:
        self.player = Player('Вася', 100, Wearpon('Меч', 10), 10, 0, 1)
        self.enemy = Player('упырь', 80, None, 5, 1, 5)
        self.is_fiting = False
        self.fight()

    def fight(self) -> None:
        self.is_fiting = True
        while self.is_fiting:
            os.system('cls')
            self.player.show()
            self.player.attack(self.enemy)
            self.enemy.show()
            self.enemy.attack(self.player)
            self.check_winer()
        print('бой окончен')

    def check_winer(self) -> None:
        if self.player.hp <= 0:
            print(self.enemy.name, 'победил')
            self.is_fiting = False
        elif self.enemy.hp <= 0:
            self.is_fiting = False
            self.player.get_award(self.enemy)

Game()