from lib import tokenizer
from lib.tokenizer import Tokenizer
import sys


def test(s: str):
    tokenizer = Tokenizer(s)
    print(tokenizer.generate_tokens())


if __name__ == "__main__":
    if "test" in sys.argv:
        test('(hello AND world) OR "python is great"')
        test('("hANDlo" AND world) OR \'python is okay\'')
        test('"(1 + 2) * 6"')
        test('(How AND ARE) OR ((A AND B) AND a)')
        test('(How AND ARE) OR (A OR(A AND B))')
        exit()

    while True:
        print("Please enter a search expression. Press Ctrl+C to exit")
        s = input()
        try:
            test(s)
        except Exception as e:
            print(str(e))
