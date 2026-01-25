"""
Design a system to simulate battles between monsters.
Each monster has a name, health points (HP), and a list of attacks it can perform. Each attack has a name and a damage value.
Implement the following:

A Monster class that can be instantiated with a name, HP, and a list of attacks
A way for one monster to attack another using one of its attacks
A way to check if a monster is still alive (HP > 0)

Example:
monster1 = Monster("Drakon", 100, [Attack("Fireball", 20), Attack("Claw", 10)])
monster2 = Monster("Gryphon", 80, [Attack("Peck", 15), Attack("Wing Slash", 25)])
monster1.attack(monster2, "Fireball")  # Gryphon's HP is now 60
monster2.is_alive()  # True
monster2.attack(monster1, "Wing Slash")  # Drakon's HP is now 75

Follow-ups to consider:
- What if an attack misses sometimes?
- How would you add type effectiveness (fire vs water, etc.)?
- How would you implement a full battle loop until one monster faints?
- How would you add status effects like poison or paralysis?
"""

from dataclasses import dataclass
import random


@dataclass
class Setup:
    attack: int
    damage: int
    miss_chance: float = 0.0


class Game:
    def __init__(self, side_one: ["Monster"], side_two: ["Monster"]):
        self.side_one = [Monster(m.attack, m.damage, m.miss_chance) for m in side_one]
        self.side_two = [Monster(m.attack, m.damage, m.miss_chance) for m in side_two]

    def fight(self) -> [str]:
        """Causes the two sides of monsters to fight each other and returns logs of the result"""
        logs = []

        if not len(self.side_one) or not len(self.side_one):
            if len(self.side_one):
                logs.append("Side two has no monsters alive. Side one wins.")
            elif len(self.side_two):
                logs.append("Side one has no monsters alive. Side two wins.")
            else:
                logs.append("No monsters left alive. It's a draw.")
        else:
            first_monster = self.side_one.pop()
            second_monster = self.side_two.pop()

            first_attack = first_monster.attack(second_monster)
            second_attack = second_monster.attack(first_monster)

            first_log = f"First monster attacks for {first_attack} damage. Second monster has {second_monster.health} health left."
            second_log = f"Second monster attacks for {second_attack} damage. First monster has {first_monster.health} health left."
            if first_attack == 0:
                first_log = f"First monster missed. Second monster has {second_monster.health} health left."
            if second_attack == 0:
                second_log = f"Second monster missed. First monster has {first_monster.health} health left."

            logs.extend([first_log, second_log])

            if not first_monster.is_alive():
                logs.append("The first monster died.")

            if not second_monster.is_alive():
                logs.append("The second monster died.")

        return logs

    def can_fight(self) -> bool:
        """Returns if there are monsters alive on both sides"""

        return len(self.side_one) > 0 and len(self.side_two) > 0


class Monster:
    def __init__(self, attack_power: int, health: int, miss_chance: float = 0.0):
        self.attack_power = attack_power
        self.health = health
        self.miss_chance = miss_chance

    def attack(self, monster: "Monster") -> int:
        """Takes in another monster to attack and deals damange to it"""
        if random.random() < self.miss_chance:
            return 0

        damage_dealt = monster.damage(self.attack_power)

        return damage_dealt

    def damage(self, attack_power: int) -> int:
        """Takes in an attack power from another monster and"""
        if self.health >= attack_power:
            self.health -= attack_power

            return attack_power
        else:
            prev_health = self.health
            self.health = 0

            return prev_health

    def is_alive(self) -> bool:
        """Returns if the monster is still alive or not"""

        return self.health > 0
