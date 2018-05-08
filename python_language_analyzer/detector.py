from abc import ABC, abstractmethod


class Detector(ABC):
    def __init__(self, file):
        """
        :param file: List of strings representing the lines of the file.
        """
        self.file = file

    @abstractmethod
    def __call__(self):
        ...
