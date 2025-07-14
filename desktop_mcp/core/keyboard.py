from typing import Protocol


class KeyboardController(Protocol):
    def write(self, text: str, interval: int = 0) -> None:
        """Prints out text with a quarter second delay after each character"""
        ...
    
    def press(self, key: str) -> None:
        """"""
        ...

    def key_down(self, key: str) -> None:
        """"""
        ...
    
    def key_up(self, key: str) -> None:
        """"""
        ...
