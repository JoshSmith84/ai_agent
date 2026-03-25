from functions.get_file_content import  get_file_content
from config import *


test_tuples = (
    ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
)


if __name__ == "__main__":
    for tup in test_tuples:
        output = get_file_content(tup[0], tup[1])
        print(f"\nTesting: {tup[1]}.. \nCharacters read: {len(output)}")
        print(output)

        if len(output) >= MAX_CHARS:
            trunc_message_index = len(output) - MAX_CHARS
            print(f"{output[-trunc_message_index:]}")