from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items = list()

    def push(self, item: Any):
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def peek(self) -> Any:
        return self.items[-1]

    def is_empty(self) -> bool:
        return not self.items
