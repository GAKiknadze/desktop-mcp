from typing import Protocol, Tuple


class ScreenController(Protocol):
    def get_size(self) -> Tuple[int, int]:
        """"""
        ...
