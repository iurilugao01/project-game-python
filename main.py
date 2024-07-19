import random

# Função lambda para rolar um dado
roll = lambda dice: random.randint(1, dice)

class CreateToken:
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
        damage = roll(self.damage_dice) + self.damage_bonus - target.armor
        if target.blocking:
            damage -= 5
        return max(damage, 0)  # Evita dano negativo

    def attack(self, target):
        hit = target.cd <= roll(20) + self.attack_bonus
        if hit:
            total_damage = self.roll_damage(target)
            target.life -= total_damage
            print(f'O ataque acertou! Causou: {total_damage} de dano.')
        else:
            print('O ataque falhou!')

    def block(self):
        self.blocking = True

# Exemplo de uso:
token1 = CreateToken("Guerreiro", 100, 8, 3, 5, 2, 15)
token2 = CreateToken("Inimigo", 50, 6, 2, 4, 1, 12)

token1.attack(token2)
token2.block()
token1.attack(token2)
token2.blocking = False  # Reseta o bloqueio após um turno (exemplo)


teste = {}


