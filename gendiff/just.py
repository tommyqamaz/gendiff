import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", file_name)


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


plain_data = (
    read(
        "/Users/g/Documents/python_projects/hexlet/python-project-lvl2/tests/fixtures/diff_plain.txt"
    )
    .rstrip()
    .split("\n\n\n")
)

print(plain_data)
