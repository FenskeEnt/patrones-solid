

def permisos(roles: list):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if 'client' in roles:
                return fn(*args, **kwargs)
            return({
                'Eror': 401,
                "Type": "Unathorized"
            })
        return wrapper
    return decorator
            

@permisos(roles=['admin', 'moderator'])
def saludar():
    return 'Hola que tal?'

func = saludar()
print(func)


