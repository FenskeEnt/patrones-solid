from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def compute_damage(self, recive_attack: str) -> int: pass

class ConcreateEnemy(Enemy):

    def compute_damage(self, recive_attack: str) -> int:
        print('Oh no, 100 de daño')
        return 100

class EnemyDecorator(Enemy):

    decorated_enemy: Enemy

    def __init__(self, enemy_to_decorate: Enemy):
        self.decorated_enemy = enemy_to_decorate

    def compute_damage(self, recive_attack: str) -> int: pass

class HelemetDecorator(EnemyDecorator):

    def compute_damage(self, recive_attack: str) -> int:
        if recive_attack == 'Daño a la cabeza':
            print('Llevo casco no me haces daño en la cabeza, daño 0')
            return 0
        print('100 de daño')
        return 100

def tipo_ataque() -> str:
    insert = int(input("""Seleccione el tipo de ataque
[1]Para atacar a la cabeza
[2]Para atacar al cuerpo
[3]Para atacar a las piernas
>>>: """))
    ataques = {
        1: 'Daño a la cabeza',
        2: 'Daño al cuerpo',
        3: 'Daño a las piernas'
    }
    return ataques[insert]

def main() -> None:

    enemigo_desnudo = ConcreateEnemy()

    enemigo_desnudo.compute_damage(tipo_ataque())

    # enemigo_con_casco = HelemetDecorator(enemigo_desnudo)

    # enemigo_con_casco.compute_damage(tipo_ataque())
    

if __name__ == '__main__':
    while True:
        main()
