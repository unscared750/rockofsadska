import random


# Třídy pro postavy a monstra
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


class Monster(Character):
    def __init__(self, name, health, attack, defense, loot):
        super().__init__(name, health, attack, defense)
        self.loot = loot

    def attack_player(self, player):
        damage = max(self.attack - player.defense, 1)
        print(f"{self.name} útočí na {player.name} a způsobuje {damage} poškození!")
        player.take_damage(damage)


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 5)
        self.inventory = []

    def attack_monster(self, monster):
        damage = max(self.attack - monster.defense, 1)
        print(f"{self.name} útočí na {monster.name} a způsobuje {damage} poškození!")
        monster.take_damage(damage)

    def pick_up_loot(self, loot):
        print(f"{self.name} našel {loot}!")
        self.inventory.append(loot)


# Funkce pro generování dungeonových místností
def generate_room():
    rooms = ["Pokoj s pokladem", "Pokoj s monstrem", "Pokoj s prázdnotou"]
    return random.choice(rooms)


def play_game():
    print("Vítejte v dungeonu!")
    name = input("Jak se jmenujete, hrdino? ")
    player = Player(name)
    print(f"Ahoj {player.name}, jsi připravený na dobrodružství?\n")

    while player.is_alive():
        room = generate_room()
        print(f"\nPřicházíte do {room}.")

        if room == "Pokoj s pokladem":
            print("Našli jste poklad!")
            loot = random.choice(["Zlato", "Magický meč", "Léčivý lektvar"])
            player.pick_up_loot(loot)

        elif room == "Pokoj s monstrem":
            monster = Monster("Ork", 50, 10, 3, "Zlato")
            print(f"V tomto pokoji na vás čeká {monster.name}!")

            while monster.is_alive() and player.is_alive():
                action = input("Chcete zaútočit (a) nebo utéct (u)? ").lower()
                if action == 'a':
                    player.attack_monster(monster)
                    if monster.is_alive():
                        monster.attack_player(player)
                elif action == 'u':
                    print("Utíkáte z boje.")
                    break
                else:
                    print("Neplatná volba, zkuste znovu.")

            if monster.is_alive() == False:
                player.pick_up_loot(monster.loot)

        elif room == "Pokoj s prázdnotou":
            print("Pokoj je prázdný. Nemáte co dělat, takže pokračujete dál.")

        if player.is_alive():
            continue_choice = input("\nChcete pokračovat dál? (ano/ne) ").lower()
            if continue_choice == 'ne':
                print(f"Děkujeme za hru, {player.name}!")
                break
        else:
            print(f"{player.name}, bohužel jsi zemřel! Konec hry.")
            break


# Spustit hru
play_game()
