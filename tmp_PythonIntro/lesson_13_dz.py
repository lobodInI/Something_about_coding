class Unit:
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intellect = intellect

    def get_level_up(self):
        raise NotImplementedError("This method must overwrite in child class")

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name=}, {self.health=}, {self.power=}, {self.agility=}, {self.intellect=}"

    def __repr__(self):
        return f"({self.name}, {self.health}, {self.power}, {self.agility}, {self.intellect})"


class Mage(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1, mage_type="Fire"):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.mage_type = mage_type

    def get_level_up(self):
        # if self.intellect < 10:
        #     self.intellect += 1
        self.intellect += int(self.intellect < 10)

    def __str__(self):
        str_unit = super().__str__()
        return f"{str_unit}, {self.mage_type=}"


mage = Mage("Gendalf", intellect=9)
# print(mage)
mage.get_level_up()
print(mage)
mage.get_level_up()
print(mage)

# unit = Unit("Jacob", intellect=5)
# unit_2 = Unit("Jack")
# units = [unit, unit_2]
# print(units)
# print(unit)
######################################
#
# class Unit:
#     name = "John"  # атрибут класса (желательно не использовать просто так )))
#
#     def __init__(self, name):
#         self.name = name  # атрибут экзаемпляра класса
#
# print(Unit.name)
#
# unit = Unit("Jacob")
# print(unit.name)




# value = 12765123784618376817635234767623123
# result = len(str(value))