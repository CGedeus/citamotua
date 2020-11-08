# Script to automatically change file characters
# and syntax.

import re
import os

class automatic_file_update:

    def __init__(self, file_name):
        self.file = file_name

    def read_write(self):
        '''
        Read and update current file(s) with new characters and syntax
        '''
        with open(self.file, 'r') as file_handler1:
            read_file = file_handler1.read()
            replace_char = read_file.replace('.', '_')

        with open(self.file, 'w') as file_handler2:
            file_write = file_handler2.write(replace_char)
            print file_write

if __name__ == '__main__':

    for root, dir, files in os.walk("C:\Users\cgede"):
        automatic_file_update.read_write(files)
