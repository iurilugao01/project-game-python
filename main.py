import random
roll = lambda dice: random.randint(1, dice)


class Create_token:
    def __init__(self, name, life, damage_dice, damage_bonus, attack_bonus, armor, cd):
        self.name = name
        self.life = life
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus
        self.attack_bonus = attack_bonus
        self.armor = armor
        self.blocking = False
        self.cd = cd

    def roll_damage(self, target):
        damage = roll(20) + self.damage_bonus - target.armor
        if target.blocking:
            damage -= 5
        return damage

 def attack(self, target):
        hit = target.cd <= roll(20) + self.attack_bonus
        if hit:
            total_damage = roll(self.damage_dice) - target.armor
            target.life -= total_damage

            print(f'o ataque acertou! causou: {total_damage} de dano')
        else:
            print('o ataque falhou!')

    def block(self):
        self.blocking = True






