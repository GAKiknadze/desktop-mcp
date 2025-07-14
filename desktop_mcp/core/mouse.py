from typing import Protocol, Tuple


class MouseController(Protocol):
    def position(self) -> Tuple[int, int]:
        "Current mouse position x and y"
        ...

    def move_to(self, x: int, y: int) -> None:
        """Move mouse to XY coordinates"""
        ...

    def move_rel(self, x: int, y: int) -> None:
        """Move mouse relative to its current position"""
        ...

    def drag_to(self, x: int, y: int) -> None:
        """Drag mouse to XY"""
        ...

    def drag_rel(self, x: int, y: int) -> None:
        """Drag mouse relative to its current position"""
        ...

    def right_click(self, x: int = None, y: int = None) -> None:
        """Mouse right click"""
        ...

    def left_click(self, x: int = None, y: int = None) -> None:
        """Mouse left click"""
        ...

    def left_double_click(self, x: int = None, y: int = None) -> None:
        """Mouse left double click"""
        ...

    def middle_click(self, x: int = None, y: int = None) -> None:
        """Mouse middle click"""
        ...

    def scroll(self, amount_to_scroll: int, x: int = None, y: int = None) -> None:
        """Positive scrolling will scroll up, negative scrolling will scroll down"""
        ...
