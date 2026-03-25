from functions.get_files_info import get_files_info

test_tuples = (
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
)


if __name__ == "__main__":
    for p_dir, dir in test_tuples:
        print(f"Result for " \
            f"{'current' if dir == "." else "'" + dir + "'"} " \
            f"directory:\n" \
            f"{get_files_info(p_dir, dir)}")