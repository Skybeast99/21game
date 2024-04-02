class Player:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = help
        self.power = 10
    

    def show(self) -> None:
        return f'игрок {self.name}, жизни: {self.hp}'



class Game:
    def __init__(self) -> None:
        self.player = Player('Вася', 100)
        self.enemy = Player('Ася', 80)

    def fight(self) -> None:
        while True:

            self.enemy.hp -= self.player.power
            print(self.player.name, 'ударил', self.enemy.name)
            print(self.player)
            if self.enemy.hp <= 0:
                break
            
            self.player.hp -= self.enemy.power
            print(self.enemy.name, 'ударил', self.player.name)
            print(self.enemy)
            if self.player.hp <= 0:
                break
        print('бой окончен')

Game()