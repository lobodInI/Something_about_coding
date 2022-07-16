from random import choice, randint

class Unit:
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intellect = intellect

    def heal(self):
        if self.health <= 5:
            self.health += 1
        elif self.health < 100:
            self.health += int(round((randint(1, 20) * 0.01) * self.health, 0))
            if self.health > 100:
                self.health = 100


    def damage(self):
        if self.health > 0:
            self.health -= int(round((randint(1, 20) * 0.01) * self.health, 0))
            if self.health < 0:
                self.health = 0

    def get_level_up(self):
        pass                 # я так розумію, що багато сенсу тут немає щось писати
                             # або raise NotImplementedError('')

    def __str__(self):
        return f"Name unit: {self.name}   quantity health: ({self.health})   hit power: ({self.power})   " \
               f"agility points: ({self.agility})   intellect points: ({self.intellect})"

class Knight(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1, weapon_type=('axe', 'sword', 'pike')):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.weapon_type = choice(weapon_type)

    def get_level_up(self):
        if self.power < 10:
            self.power += 1

    def __str__(self):
        unit_str = super().__str__()
        return f'Class unit: Knight\n{unit_str}\nselected weapon: {self.weapon_type}'

class Archer(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1, archers_weapon=('sling', 'crossbow', 'bow')):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.archers_weapon = choice(archers_weapon)

    def get_level_up(self):
        if self.agility < 10:
            self.agility += 1

    def __str__(self):
        unit_str = super().__str__()
        return f'Class unit: Archer\n{unit_str}\nselected archer\'s weapon: {self.archers_weapon}'

class Mage(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1, type_magic=('water', 'fire', 'air')):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.type_magic = choice(type_magic)

    def get_level_up(self):
        if self.intellect < 10:
            self.intellect += 1

    def __str__(self):
        unit_str = super().__str__()
        return f'Class unit: Mage\n{unit_str}\nselected type magic: {self.type_magic}'

frodo = Unit(name='Frodo')
aragorn = Knight(name='Aragorn')
print(aragorn)
aragorn.damage()
aragorn.damage()
aragorn.damage()
aragorn.heal()
aragorn.get_level_up()
aragorn.get_level_up()
aragorn.get_level_up()
print('')
print(aragorn)
print('*-'*25)
legolas = Archer(name='Legolas')
print(legolas)
legolas.damage()
legolas.damage()
legolas.damage()
legolas.heal()
legolas.get_level_up()
legolas.get_level_up()
legolas.get_level_up()
print('')
print(legolas)
print('*-'*25)
gendalf = Mage(name='Gendalfe')
print(gendalf)
gendalf.damage()
gendalf.damage()
gendalf.damage()
gendalf.heal()
gendalf.get_level_up()
gendalf.get_level_up()
gendalf.get_level_up()
print('')
print(gendalf)

