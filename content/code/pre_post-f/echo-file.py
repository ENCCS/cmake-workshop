import sys

# for simplicity we do not verify the number and
# type of arguments
file_path = sys.argv[-1]

try:
    with open(file_path, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(f'ERROR: file {file_path} not found')
