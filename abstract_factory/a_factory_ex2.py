from abc import ABC, abstractmethod

class Background(ABC):

    @abstractmethod
    def create_bg(self): pass

class DarkBackground(Background):

    def create_bg(self):
        return 'Se ha creado un fondo oscuro para la app'

class LightBackground(Background):

    def create_bg(self):
        return 'Se ha creado un fondo claro para la app'

class AbstractFactory(ABC):

    @abstractmethod
    def create_bg(self) -> Background: pass

    @abstractmethod
    def create_side_bar(self): pass

    @abstractmethod
    def create_nav(self): pass

class DarkThemeFactory(AbstractFactory):

    def create_bg(self):
        return DarkBackground()

    def create_side_bar(self):
        return 'Se ha creado una sidebar oscura para la app'

    def create_nav(self):
        return 'Se ha creado una navegacion oscura para la app'

class LightThemeFactory(AbstractFactory):

    def create_bg(self):
        return LightBackground()

    def create_side_bar(self):
        return 'Se ha creado una sidebar clara para la app'

    def create_nav(self):
        return 'Se ha creado una navegacion clara para la app'

        
    
