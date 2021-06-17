from enum import Enum


class Operator(Enum):
    AND = "AND"
    OR = "OR"

    @staticmethod
    def values():
        return (e.value for e in Operator)


class Paranthesis(Enum):
    OPEN = "("
    CLOSE = ")"

    @staticmethod
    def values():
        return (e.value for e in Paranthesis)


class OperatorPrecedence(Enum):
    AND = 1
    OR = 0

    @staticmethod
    def get_precedence(operator: str):
        if operator not in Operator.values():
            raise ValueError(f"Invalid operator `{operator}`")

        return getattr(OperatorPrecedence, operator, None).value


class TokenType(Enum):
    OPERATOR = "OPERATOR"
    PARANTHESIS = "PARANTHESIS"
    OPERAND = "OPERAND"

    @staticmethod
    def get_token_type(token: str):
        if token in Operator.values():
            return TokenType.OPERATOR

        elif token in Paranthesis.values():
            return TokenType.PARANTHESIS

        return TokenType.OPERAND
