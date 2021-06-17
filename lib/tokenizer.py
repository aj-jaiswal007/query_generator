from lib.utils import unquote_string
from lib.enums import Operator, Paranthesis, TokenType
import re


class Tokenizer:
    def __init__(self, _query: str) -> None:
        self._query = _query

    def _get_raw_tokens(self) -> list:
        """Returns a list of tokens
        For eg:
            IP: ("Hello" OR 'python is good')

            OP: [ ( , "Hello", OR, 'python is good' ] 
        """
        return re.findall(r"""AND|OR|[\(\)]|\w+|".+"|'.+'""", self._query)

    def _get_sanitized_tokens(self) -> list:
        sanitized_tokens = list()
        for token in self._get_raw_tokens():
            if token in Operator.values() or token in Paranthesis.values():
                sanitized_tokens.append(token)
            else:
                sanitized_tokens.append(unquote_string(token))

        return sanitized_tokens

    def _validate_expression(self, token_list: list):
        """Validates if the token list is a valid query
        Raises AssertionError if expression not valid

        NOTE: This is not the best expression validator, modify it later
        """
        open_bracket_visited = 0
        prev_type = None
        prev_item = None
        for item in token_list:
            curr_type = TokenType.get_token_type(item)
            if curr_type == TokenType.PARANTHESIS:
                if item == Paranthesis.CLOSE.value:
                    assert open_bracket_visited, f"`)` found without an opening paranthesis"
                    assert prev_type != TokenType.OPERATOR, f"`)` used after an operator. You mad bro?"
                    open_bracket_visited -= 1
                else:
                    # open paranthesis
                    open_bracket_visited += 1

            elif prev_type:
                # no consecutive operator or operand should be present
                assert (
                    curr_type != prev_type
                ), 'Consecutive {0} found, did you forget to add {1}?'.format(
                    curr_type.value,
                    'quotes " "' if curr_type == TokenType.OPERAND else 'a search string'
                )
                if curr_type == TokenType.OPERATOR:
                    assert(
                        prev_item != Paranthesis.OPEN.value
                    ), "'(' found before an operator, did you forget to add a search string? {}".format(self._query)

            prev_type = curr_type
            prev_item = item

        assert not open_bracket_visited, f"`(` found without a closing paranthesis"

    def generate_tokens(self) -> list:
        tokens = self._get_sanitized_tokens()
        self._validate_expression(tokens)
        return tokens
