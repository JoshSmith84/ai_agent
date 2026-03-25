from functions.get_files_info import get_files_info

test_tuples = (
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
)


if __name__ == "__main__":
    for tup in test_tuples:
        print(f"Result for " \
            f"{'current' if tup[1] == "." else "'" + tup[1] + "'"} " \
            f"directory:\n" \
            f"{get_files_info(tup[0], tup[1])}")