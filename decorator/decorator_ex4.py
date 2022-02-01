from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def compute_damage(self, recive_attack: str) -> int: pass

class EnemyDecorator(Enemy):

    decorated_enemy: Enemy

    def __init__(self, enemy_to_decorate: Enemy):
        self.decorated_enemy = enemy_to_decorate

    def compute_damage(self, recive_attack: str) -> int: pass

def helemet_decorator(cls):
    def wrapper(*args, **kwargs):
        def new_compute_damage(self, recive_attack: str) -> int:
            if recive_attack == 'Daño a la cabeza':
                print('Enemigo con casco daño 0')
                return 0
            print('Enemigo con casco, daño 100')
            return 100
        setattr(cls, 'compute_damage', new_compute_damage)
        return cls(*args, **kwargs)
    return wrapper

def armour_decorator(cls):
    def wrapper(*args, **kwargs):
        def new_compute_damage(self, recive_attack: str) -> int:
            if recive_attack == 'Daño al cuerpo':
                print('Enemigo con armadura daño 0')
                return 0
            print('Enemigo con armadura, daño 100')
            return 100
        setattr(cls, 'compute_damage', new_compute_damage)
        return cls(*args, **kwargs)
    return wrapper

def set_items(items: list):
    def decorator(cls):
        def wrapper(*args, **kwargs):
            def new_compute_damage(self, recive_attack: str) -> int:
                if recive_attack in items:
                    print('Daño 0')
                    return 0
                print('Daño 100')
                return 100
            setattr(cls, 'compute_damage', new_compute_damage)
            return cls(*args, **kwargs)
        return wrapper
    return decorator

# def choice_decorator():
#     insert = int(input("""Con que desea equipar al enemigo
# [1]Para equiparlo con casco
# [2]Para equiparlo con armadura
# >>>: """))
#     equipamiento = {
#         1: helemet_decorator,
#         2: armour_decorator
#     }
#     return equipamiento[insert]

def choice_decorator() -> list:
    choosing: bool = True
    items: list = []
    while choosing:
        insert = int(input("""Con que desea equipar al enmigo
[1]Para equiparlo con casco
[2]Para equiparlo con armadura
[3]Para equiparlo con pantalones
[4]Para atacar al enemigo
>>>: """))
        protecciones = {
            1: 'Daño a la cabeza',
            2: 'Daño al cuerpo',
            3: 'Daño a las piernas'
        }
        if insert != 4:
            items.append(protecciones[insert])
        if insert == 4:
            choosing = False
            return items



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

# @choice_decorator()
@set_items(choice_decorator())
class ConcreateEnemy(Enemy):

    def compute_damage(self, recive_attack: str) -> int:
        print('Enemigo desnudo, 100 de daño')
        return 100

def main() -> None:

    enemigo_concreto = ConcreateEnemy()

    enemigo_concreto.compute_damage(tipo_ataque())

if __name__ == '__main__':
    while True:
        main()