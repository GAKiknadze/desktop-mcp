from typing import Protocol, Tuple


class MouseController(Protocol):
    def mouse_position(self) -> Tuple[int, int]:
        "Current mouse position x and y"
        ...

    def mouse_move_to(self, x: int, y: int):
        """Move mouse to XY coordinates"""
        ...

    def mouse_move_rel(self, x: int, y: int):
        """Move mouse relative to its current position"""
        ...

    def mouse_drag_to(self, x: int, y: int):
        """Drag mouse to XY"""
        ...

    def mouse_drag_rel(self, x: int, y: int):
        """Drag mouse relative to its current position"""
        ...

    def mouse_right_click(self, x: int = None, y: int = None):
        """Mouse right click"""
        ...

    def mouse_left_click(self, x: int = None, y: int = None):
        """Mouse left click"""
        ...

    def mouse_left_double_click(self, x: int = None, y: int = None):
        """Mouse left double click"""
        ...

    def mouse_middle_click(self, x: int = None, y: int = None):
        """Mouse middle click"""
        ...

    def mouse_scroll(self, amount_to_scroll: int, x: int = None, y: int = None):
        """Positive scrolling will scroll up, negative scrolling will scroll down"""
        ...
