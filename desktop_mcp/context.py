from dataclasses import dataclass

from . import core


@dataclass
class AppContext:
    keyboard: core.KeyboardController
    mouse: core.MouseController
    # screen: core.ScreenController
    # system: core.SystemController
    # window: core.WindowController
