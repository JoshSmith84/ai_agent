from functions.write_file import write_file


test_tuples = (
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
)
if __name__ == "__main__":
    for dir, file, content in test_tuples:
        status = write_file(dir, file, content)

        print(status)
