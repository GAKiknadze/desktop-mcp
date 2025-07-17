from typing import Tuple
import pyautogui


class ScreenController:
    def get_size(self) -> Tuple[int, int]:
        """"""
        return pyautogui.size()
