from lib.query_generators.sql_generator import SQLQueryGenerator
from lib.query_generators.mongo_generator import MongoQueryGenerator
from lib.tokenizer import Tokenizer
import sys


def test(query: str, table: str = "Resume", column: str = "text"):
    tokenizer = Tokenizer(query)
    tokens_list = tokenizer.generate_tokens()
    mongo_gen = MongoQueryGenerator(
        table_name=table,
        column_name=column,
        token_list=tokens_list
    )
    sql_gen = SQLQueryGenerator(
        table_name=table,
        column_name=column,
        token_list=tokens_list
    )
    print("-------------------------------------------------------------------------------")
    print("ORIGINAL STRING:")
    print(query)
    print()
    print("MONGO FILTER QUERY DICT:")
    print(mongo_gen.evaluate_expression())
    print()
    print("SQL QUERY:")
    print('SELECT * FROM "{}" WHERE {} ;'.format(
        table,
        sql_gen.evaluate_expression()
    ))
    print()


if __name__ == "__main__":
    if "test" in sys.argv:
        test('(hello AND world) OR "python is great"')
        test('"python is great"')
        test('("hANDlo" AND world) OR \'python is okay\'')
        test('"(1 + 2) * 6"')
        test('(How AND ARE) OR ((A AND B) AND a)')
        test('(How AND ARE) OR (A OR(A AND B))')
        exit()

    table_name = input("Enter DB table name: ")
    column_name = input("Enter DB column name to search: ")
    while True:
        print("Please enter a search expression. Press Ctrl+C to exit")
        s = input()
        try:
            test(s, table_name, column_name)
        except Exception as e:
            print(str(e)+"\n")
