from typing import Tuple

import pyautogui


class MouseController:
    def position(self) -> Tuple[int, int]:
        """Current mouse position x and y"""
        x, y = pyautogui.position()
        return x, y

    def move_to(self, x: int, y: int) -> None:
        """Move mouse to XY coordinates"""
        pyautogui.moveTo(x, y)

    def move_rel(self, x: int, y: int) -> None:
        """Move mouse relative to its current position"""
        pyautogui.moveRel(x, y)

    def drag_to(self, x: int, y: int) -> None:
        """Drag mouse to XY"""
        pyautogui.dragTo(x, y)

    def drag_rel(self, x: int, y: int) -> None:
        """Drag mouse relative to its current position"""
        pyautogui.dragRel(x, y)

    def right_click(self, x: int = None, y: int = None) -> None:
        """Mouse right click"""
        pyautogui.rightClick(x, y)

    def left_click(self, x: int = None, y: int = None) -> None:
        """Mouse left click"""
        pyautogui.leftClick(x, y)

    def left_double_click(self, x: int = None, y: int = None) -> None:
        """Mouse left double click"""
        pyautogui.doubleClick(x, y)

    def middle_click(self, x: int = None, y: int = None) -> None:
        """Mouse middle click"""
        pyautogui.middleClick(x, y)

    def scroll(self, amount_to_scroll: float, x: int = None, y: int = None) -> None:
        """Positive scrolling will scroll up, negative scrolling will scroll down"""
        pyautogui.scroll(amount_to_scroll, x, y)
