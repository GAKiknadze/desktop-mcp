from typing import Protocol

class SystemController(Protocol):
    def system_info(self):
        pass
