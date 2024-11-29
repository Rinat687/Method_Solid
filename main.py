from abc import ABC, abstractmethod
import random

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def damage(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

    def damage(self):
        return random.randint(15, 25)  # Урон меча

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

    def damage(self):
        return random.randint(10, 20)  # Урон лука

# Класс Monster
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"Монстр получает урон. Осталось здоровья: {self.health}")

# Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        if isinstance(new_weapon, Weapon) and new_weapon != self.weapon:
            self.weapon = new_weapon
            print(f"{self.name} сменил оружие на {type(new_weapon).__name__}.")
        else:
            print("Оружие не изменено.")

    def attack(self, monster: Monster):
        if monster.health > 0:
            print(self.weapon.attack())
            monster.take_damage(self.weapon.damage())  # Наносим урон в зависимости от типа оружия
        else:
            print("Монстр уже побежден!")

# Реализация боя
def battle(fighter: Fighter, monster: Monster):
    while monster.health > 0:
        fighter.attack(monster)
        if monster.health <= 0:
            print("Монстр побежден!")
            break

# Пример использования программы
if __name__ == "__main__":
    fighter = Fighter("Воин", Sword())
    monster = Monster(100)

    battle(fighter, monster)

    fighter.change_weapon(Bow())
    monster.health = 100  # Восстанавливаем здоровье монстра
    battle(fighter, monster)