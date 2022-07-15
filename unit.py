import random

class Unit():
    """Загальний опис юніта"""
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 1
        self.dexterity = 1
        self.intellect = 1

    def __str__(self):
        return f'Hello my friend {self.name}\nWelcome in standard class \'Unit\'\nYou can choose one of three classes '\
               f'of warriors: mage, archer, knight\nThe initial values of each warrior:\nHealth = {self.health} ' \
               f'\nPower = {self.power}\nDexterity =  {self.dexterity}\nIntellect =  {self.intellect} '

    def heal(self):
        """Лікування юніта"""
        if self.health < 100:
            self.health += int(round((random.randint(1, 20) * 0.01) * self.health, 0))
            if self.health > 100:
                self.health = 100
            elif self.health <= 5:
                self.health += 1
            return f'I feel a surge of strength, now my health level: {self.health}'
        else:
            return 'How do you imagine that? I\'m healthy'

    def damage(self):
        """Втрата здоров'я юнітом"""
        if self.health > 0:
            self.health -= int(round((random.randint(1, 20) * 0.01) * self.health, 0))
            if self.health < 0:
                self.health = 0
            return f'I missed a couple of hits, my health level now: {self.health}'
        else:
            return 'Whoa, take it easy, I\'m already dead.'

    def get_level_up(self):
        if self.power < 10 and self.dexterity < 10 and self.intellect < 10:
            self.power += 1
            self.dexterity += 1
            self.intellect += 1
            return f'Your skill is rolled to 1'
        else:
            return f'Your skill is maxed out'


class Knight(Unit):
    """Створюємо клас воїна"""
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        weapon_knight = ['sword', 'axe', 'pike']
        self.weapon_knight = random.choice(weapon_knight)

    def get_level_up(self):
        if self.power < 10 and self.dexterity < 10 and self.intellect < 10:
            self.power += 1
            self.dexterity = 1
            self.intellect = 1
            return f'My skill is rolled to 1'
        else:
            return f'My skill is maxed out'

    def __str__(self):
        return f'My name is {self.name}, quantity of health: ({self.health}), power value: ({self.power}), ' \
               f'dexterity value: ({self.dexterity}), intellect value: ({self.intellect}), ' \
               f'my weapon of choice in this battle: {self.weapon_knight}.'


class Archer(Unit):
    """Створюємо клас лучника"""
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        weapon_archer = ['bow', 'crossbow', 'sling']
        self.weapon_archer = random.choice(weapon_archer)

    def get_level_up(self):
        if self.power < 10 and self.dexterity < 10 and self.intellect < 10:
            self.power = 1
            self.dexterity += 1
            self.intellect = 1
            return f'My skill is rolled to 1'
        else:
            return f'My skill is maxed out'

    def __str__(self):
        return f'My name is {self.name}, quantity of health: ({self.health}), power value: ({self.power}), ' \
               f'dexterity value: ({self.dexterity}), intellect value: ({self.intellect}), ' \
               f'I\'ll scout the area, take this weapon: {self.weapon_archer}.'

class Mage(Unit):
    """Створюємо клас мага"""
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        weapon_mage = ['air', 'fire', 'water']
        self.weapon_mage = random.choice(weapon_mage)

    def get_level_up(self):
        if self.power < 10 and self.dexterity < 10 and self.intellect < 10:
            self.power = 1
            self.dexterity = 1
            self.intellect += 1
            return f'My skill is rolled to 1'
        else:
            return f'My skill is maxed out'

    def __str__(self):
        return f'My name is {self.name}, quantity of health: ({self.health}), power value: ({self.power}), ' \
               f'dexterity value: ({self.dexterity}), intellect value: ({self.intellect}), ' \
               f'I will use the power of this element: {self.weapon_mage}.'


if __name__ == '__main__':

    welcome = Unit('Frodo')
    print(welcome)
    print('')
    aragorn = Knight('Aragorn')
    print(aragorn)
    print(aragorn.get_level_up())
    print(aragorn.get_level_up())
    print(aragorn.damage())
    print(aragorn.damage())
    print(aragorn.damage())
    print(aragorn.heal())
    print(aragorn)
    print('')
    print('* '*25)
    print('')
    legolas = Archer('Legolase')
    print(legolas)
    print(legolas.get_level_up())
    print(legolas.get_level_up())
    print(legolas.damage())
    print(legolas.damage())
    print(legolas.damage())
    print(legolas.heal())
    print(legolas)
    print('')
    print('* ' * 25)
    print('')
    gendalfe = Mage('Gendalfe')
    print(gendalfe)
    print(gendalfe.get_level_up())
    print(gendalfe.get_level_up())
    print(gendalfe.damage())
    print(gendalfe.damage())
    print(gendalfe.damage())
    print(gendalfe.heal())
    print(gendalfe)
