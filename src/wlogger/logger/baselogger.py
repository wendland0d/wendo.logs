from abc import ABC, abstractmethod


class BaseLogger(ABC):
    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warning(self):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def critical(self):
        pass

    def update_settings(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
