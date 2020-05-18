#Test script to automate testing
# May 16, 2020  -  Carson Gedeus

import re

def main():

    filename = "/Users/carsongedeus/Desktop/test_file.txt"

    with open(filename, "r") as file_handler1:
        read_file = file_handler1.read()
        replace_char = read_file.replace('.', '_')
        
    with open(filename, "w") as file_handler2:
        file_write = file_handler2.write(replace_char)

if __name__ == "__main__":
    main()
