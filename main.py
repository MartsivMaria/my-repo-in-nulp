"""
Модуль містить класи Fighter and Fight для імітації поєдинків між бійцями.
"""


class Fighter:
    """
    Клас Fighter представляє бійця в поєдинку.
    """

    def __init__(self, fighter_name, health, damage_per_attack, *args):
        """
        Ініціалізація бійця з вказанням основних характеристик.
        """
        self.name = fighter_name
        self.health = health
        self.damage_per_attack = damage_per_attack
        self.public_numeric_field = args[0]
        self.public_string_field = args[1]

    def get_fighter_name(self):
        """
        Повертає ім'я бійця.
        """
        return self.name

    def get_damage_per_attack(self):
        """
        Повертає кількість шкоди, яку бієць завдає під час атаки.
        """
        return self.damage_per_attack

    def get_health(self):
        """
        Повертає поточне здоров'я бійця.
        """
        return self.health

    def is_alive(self):
        """
        Перевіряє за станом здоров'я чи бієць живий.
        """
        return self.health >= 0

    def attack(self, opponent):
        """
        Атака на супротивника.
        """
        opponent.health -= self.damage_per_attack
        return self.health

    def get_numeric_field(self):
        """
        Повертає значення числового поля бійця.
        """
        return self.public_numeric_field

    def get_string_field(self):
        """
        Повертає значення строкового поля бійця.
        """
        return self.public_string_field


class Fight:
    """
    Клас Fight представляє поєдинок двох бійців.
    """

    def __init__(self, fighter1, fighter2):
        """
        Ініціалізація поєдинку із заданими бійцями.
        """
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def get_fighter_1(self):
        """
        Бієць 1
        """
        return self.fighter1

    def get_winner(self):
        """
        Визначає переможця
        """
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            self.fighter1.attack(self.fighter2)
            self.fighter2.attack(self.fighter1)
            if not self.fighter2.is_alive():
                return self.fighter1.name

            if not self.fighter1.is_alive():
                return self.fighter2.name

            if not self.fighter1.is_alive() and not self.fighter2.is_alive():
                return None
        return None


fighter_1 = Fighter("боєць 2", 70, 40, 1, "some_string")
fighter_2 = Fighter("боєць 1", 90, 50, 2, "another_string")

fight = Fight(fighter_1, fighter_2)
winner = fight.get_winner()

if winner is not None:
    print(f"{winner} переміг!")
else:
    print("Нічия")
