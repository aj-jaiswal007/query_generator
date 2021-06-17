from .base import BaseQueryGenerator


class MongoQueryGenerator(BaseQueryGenerator):
    def __init__(self, table_name: str, column_name: str, token_list: list):
        super().__init__(table_name, column_name, token_list)
