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
    for dir, file in test_tuples:
        output = get_file_content(dir, file)
        print(f"\nTesting: {file}.. \nCharacters read: {len(output)}")
        print(output)

        if len(output) > MAX_CHARS:
            trunc_message_index = len(output) - MAX_CHARS
            print(f"{output[-trunc_message_index:]}")