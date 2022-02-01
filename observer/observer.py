from abc import ABC, abstractmethod
import time

class Observer(ABC):

    @abstractmethod
    def update(self): pass

class Observable(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None: ...

    @abstractmethod
    def detach(self, observer: Observer) -> None: ...

    @abstractmethod
    def notify(self): ...

class YoutuneChannel(Observable):

    __channel_suscribers: list = []
    __last_video_posted: str = ''

    def attach(self, observer: Observer) -> None:
        self.__channel_suscribers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__channel_suscribers.remove(observer)

    def notify(self):
        for suscriber in self.__channel_suscribers:
            suscriber.update()

    def add_new_video(self, title: str) -> None:
        self.__last_video_posted = title
        self.notify()
        print(f'New youtube video added to channel')

    @property
    def last_video_posted(self):
        return self.__last_video_posted

class Suscriptor(Observer):

    def __init__(self, observable: YoutuneChannel):
        self.observable = observable

    def update(self) -> None:
        print('Nuevo video')
        print(f'{self.observable.last_video_posted}')


canal = YoutuneChannel()
sus1 = Suscriptor(canal)
sus2 = Suscriptor(canal)
sus3 = Suscriptor(canal)

canal.attach(sus1)
canal.attach(sus2)
canal.attach(sus3)

canal.add_new_video('Patrones de diseño')

time.sleep(10)

canal.add_new_video('Patrones de diseño 2')