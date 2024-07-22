import random

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
        self.dodging = False
        self.cd = cd

    def attack(self, target):
        if self.blocking:
            self.blocking = False

        if self.dodging:
            self.dodging = False

        attack_value = roll(20) + self.attack_bonus
        damage_value = roll(self.damage_dice) + self.damage_bonus

        if attack_value - self.attack_bonus == 20:
            damage_value *= 2

        if target.blocking:
            damage_value -= 3

        if target.dodging:
            hit = target.cd + 3 <= attack_value
        else:
            hit = target.cd <= attack_value

        if hit:
            total_damage = max(damage_value - target.armor, 0)
            target.life -= total_damage
            print(f'O ataque acertou! Causou: {total_damage} de dano.')
        else:
            print('O ataque falhou!')

    def block(self):
        self.blocking = True

    def dodge(self):
        self.dodging = True


class Warrior(CreateToken):
    def __init__(self, name):
        super().__init__(name, life=30, damage_dice=10, damage_bonus=2, attack_bonus=2, armor=2, cd=14)


class Assasin(CreateToken):
    def __init__(self, name):
        super().__init__(name, life=20, damage_dice=12, damage_bonus=5, attack_bonus=5, armor=0, cd=12)


class Tank(CreateToken):
    def __init__(self, name):
        super().__init__(name, life=50, damage_dice=6, damage_bonus=0, attack_bonus=0, armor=5, cd=16)


def player_chose():
    name = input('Digite o nome do seu personagem: ')
    option = input('Escolha a classe do seu personagem: \n1-Guerreiro \n2-Assassino \n3-Tanque \n')

    create_token = {
        '1': Warrior(name),
        '2': Assasin(name),
        '3': Tank(name)
    }
    return create_token[option]


print('Criando o personagem do jogador 1:')
player1 = player_chose()

print('Criando o personagem do jogador 2:')
player2 = player_chose()


def verify_placar():
    if player1.life <= 0:
        print(f'A vitória foi do {player2.name}!')
        return False
    elif player2.life <= 0:
        print(f'A vitória foi do {player1.name}!')
        return False
    return True


def menu(player, target):
    print(f'Ação de {player.name} \nVida atual: {player.life} \nCD atual: {player.cd} \nArmadura atual: {player.armor}')

    options = {
        '1': lambda: player.attack(target),  # Chama attack com target
        '2': player.dodge,
        '3': player.block
    }

    chose = input('Digite sua ação: \n1-Ataque \n2-Esquivar \n3-Bloquear \n')

    if chose in options:
        options[chose]()
    else:
        print("Ação inválida, tente novamente.")


while verify_placar():
    menu(player1, player2)
    if not verify_placar():
        break
    menu(player2, player1)
