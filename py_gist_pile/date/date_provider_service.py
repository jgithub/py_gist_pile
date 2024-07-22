from abc import ABC, abstractmethod


class DateProviderService(ABC):
    @abstractmethod
    def get_now(self):
        pass
