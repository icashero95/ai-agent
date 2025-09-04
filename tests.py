# python
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions import config

def main():
    print("Result for file content 'main.py':")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Result for file content 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Result for file content '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Result for file content 'pkg/does_not_exist.py':")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()
if __name__ == "__main__":
    main()