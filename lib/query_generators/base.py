from typing import Any
from lib.enums import Operator, OperatorPrecedence as OP, Paranthesis, TokenType
from lib.stack import Stack


class BaseQueryGenerator:
    def __init__(self, table_name: str, column_name: str, token_list: list):
        self._table_name = table_name
        self._column_name = column_name
        self._token_list = self.querytize_token_list(token_list)

    def querytize_token_list(self, token_list: list) -> list:
        res = list()
        for token in token_list:
            token_type = TokenType.get_token_type(token)
            if token_type == TokenType.OPERAND:
                res.append(self.text_to_query(token))

            else:
                res.append(token)

        return res

    def evaluate_expression(self) -> Any:
        """INFIX Expression algorithm"""
        operators = Stack()
        values = Stack()

        for token in self._token_list:

            if token not in Operator.values() and token not in Paranthesis.values():
                # Operand
                values.push(token)

            elif token == Paranthesis.OPEN.value:
                operators.push(token)

            elif token == Paranthesis.CLOSE.value:
                while operators.peek() != Paranthesis.OPEN.value:
                    output = self.perform_operation(values, operators)
                    values.push(output)

                # removing open paranthesis
                operators.pop()

            elif token in Operator.values():
                # AND or OR
                while (not operators.is_empty()) and OP.get_precedence(token) <= OP.get_precedence(operators.peek()):
                    output = self.perform_operation(values, operators)
                    values.push(output)

                operators.push(token)

        while not operators.is_empty():
            output = self.perform_operation(values, operators)
            values.push(output)

        return values.pop()

    def perform_operation(self, values: Stack, operators: Stack) -> Any:
        """This method applies AND | OR operation on values stack
        This needs to be implemented in respective DB Query Language
        """
        raise NotImplementedError(
            "`perform_operation` method not implemented in class: {}".format(
                self.__class__.__name__
            )
        )

    def text_to_query(self, value: str) -> Any:
        """This method converts text to sub-query
        This needs to be implemented in respective DB Query Language
        """
        raise NotImplementedError(
            "`text_to_query` method not implemented in class: {}".format(
                self.__class__.__name__
            )
        )
