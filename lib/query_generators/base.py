class BaseQueryGenerator:
    def __init__(self, table_name: str, column_name: str, token_list: list):
        self._table_name = table_name
        self._column_name = column_name
        self._token_list = token_list

    def _evaluate_expression(self):
        """INFIX Expression algorithm"""
        pass
