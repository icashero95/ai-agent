# python
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions import config

def main():
    print("Result for writing to 'lorem.txt':")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()

    print("Result for writing to 'pkg/morelorem.txt':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()

    print("Result for writing to '/tmp/tmp.txt':")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print()

if __name__ == "__main__":
    main()