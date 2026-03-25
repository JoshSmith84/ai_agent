from functions.run_python_file import run_python_file

test_tuples = (
    ("calculator", "main.py", None),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py", None),
    ("calculator", "../main.py", None),
    ("calculator", "nonexistent.py", None),
    ("calculator", "lorem.txt", None),
)

if __name__ == "__main__":
    for dir, file, arg in test_tuples:
        print(run_python_file(dir, file, arg))