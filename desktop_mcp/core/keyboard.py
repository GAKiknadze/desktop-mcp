import pyautogui


class KeyboardController:
    def write(self, text: str, interval: float = 0.1) -> None:
        """Prints out text with a quarter second delay after each character"""
        pyautogui.write(message=text, interval=interval)

    def press(self, key: str) -> None:
        """"""
        pyautogui.press(keys=key)

    def key_down(self, key: str) -> None:
        """"""
        pyautogui.keyDown(key=key)

    def key_up(self, key: str) -> None:
        """"""
        pyautogui.keyUp(key=key)
