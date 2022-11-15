class Hero :
    Head = 1
    abulity = True
    def __init__(self, name, nickname, hp:int, damage):
        self.name=name
        self.nickname=nickname
        self.hp=hp
        self.damage=damage
    def heal(self):
        print(self.hp + 100)
    def two_damage(self):
        print(self.damage * 2)
    def dreetings(self):
        print(f'my name is {self.name}')
    def brand_phras(self):
        print('good will win')

    def __Gen_x(self):
        ...

class Air(Hero):
    head=1
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly=fly

    def brand_phras(self):
        self.fly=True
        print('fly in the True_phrase')

class Erth(Hero):
    head=1
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly=fly

    def brand_phras(self):
        self.fly=True
        print('fly in the True_phrase')

    def __Gen_x(self):
        ...


class Space(Hero):
    head=1
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly=fly

    def brand_phras(self):
        self.fly=True
        print('fly in the True_phrase')

    def __Gen_x(self):
        ...

hero1=Erth('Alihan', 'Alihan123', 20, 1000000)
hero2=Space('Bakai', 'Bakai123', 250, 545)
hero3=Air('Ivan', 'Ivan123', 34, 543)
hero1.brand_phras()
print(hero1.fly)