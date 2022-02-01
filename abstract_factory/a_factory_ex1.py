from _typeshed import StrPath
from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def show(self) -> str: pass

class Mail(ABC):

    @abstractmethod
    def show(self) -> str: pass

class GoogleCloudStorage(CloudStorage):

    def show(self) -> str:
        return 'show Google cloud storage info'

class MicrosoftCloudStorage(CloudStorage):

    def show(self) -> str:
        return 'show Microsoft cluud storage info'

class GoogleMail(Mail):

    def show(self) -> str:
        return 'show Google mail info'

class MicrosoftMail(Mail):

    def show(self) -> str:
        return 'show Microsoft mail info'

class AbstractFactory(ABC):

    @abstractmethod
    def create_cloud_storage(self) -> CloudStorage: pass

    @abstractmethod
    def create_mail(self) -> Mail: pass

class GoogleFactory(AbstractFactory):

    def create_cloud_storage(self) -> CloudStorage:
        return GoogleCloudStorage()

    def create_mail(self) -> Mail:
        return GoogleMail()

class MicrosoftFactory(AbstractFactory):

    def create_cloud_storage(self) -> CloudStorage:
        return MicrosoftCloudStorage()

    def create_mail(self) -> Mail:
        return MicrosoftMail()

        