from typing import Any
from lib.stack import Stack
from .base import BaseQueryGenerator


class MongoQueryGenerator(BaseQueryGenerator):
    def __init__(self, table_name: str, column_name: str, token_list: list):
        super().__init__(table_name, column_name, token_list)

    def perform_operation(self, values: Stack, operators: Stack) -> Any:
        """Apply AND | OR operator on values
        """
        a = values.pop()
        b = values.pop()
        op = operators.pop().lower()
        return {
            f"${op}": [b, a]
        }

    def text_to_query(self, value: str) -> Any:
        """Create mongo query from text"""
        return {self._column_name: {"$regex": value, "$options": "i"}}
