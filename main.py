import sys
from generate_content import generate_content

def main():
    print("Hello from ai-agent!")
    if len(sys.argv) < 2:
        print("No prompt arguments provided.")
        sys.exit(1)
    return generate_content()



if __name__ == "__main__":
    main()
