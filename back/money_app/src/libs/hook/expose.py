from typing import Any
from .decore import hook

class Demo:
    def _prepare(self, *args: Any, **kwargs: Any) -> None:
        print("[PREPARE] args:", args, "kw:", kwargs)

    def _finalize(self, result: Any, *args: Any, **kwargs: Any) -> None:
        print("[FINALIZE] result =", result)

    @hook(before='_prepare', after='_finalize')
    def compute(self, x: int, y: int) -> int:
        """Простая арифметика."""
        return (x + y) * 2


if __name__ == '__main__':
    d = Demo()
    print("=>", d.compute(3, 4))
