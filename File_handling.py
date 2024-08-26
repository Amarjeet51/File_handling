# Q1) Create new text file and write a few lines of text into it

file_name = 'sample.txt'

content = """Hello there!
This is a sample text file created using Python.
Have a great day!"""

with open(file_name, 'w') as file:
    file.write(content)

     

# Q2) Open and Read the contents of the file you just created
with open(file_name, 'r') as file:
    file_contents = file.read()

file_contents

     


# Q3) Add additional text to the existing file without deleting the current content

new_content = "\nThis line has been added later as an update."

with open(file_name, 'a') as file:
    file.write(new_content)


     

# Q4) Read and print each line from the file one by one

with open(file_name, 'r') as file:
    for line in file:
        print(line.strip())

     


# Q5) Write the contents of a list to a file with each item on a new line

sample_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

list_file = 'list_contents.txt'

with open(list_file, 'w') as file:
    for item in sample_list:
        file.write(item + '\n')


     

# Q6)

with open('list_contents.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

print(lines)

     


# Q7) Count the total number of words in the file

with open('sample.txt', 'r') as file:
    content = file.read()

words = content.split()

word_count = len(words)

print(f"Total number of words: {word_count}")

     


# Q8) Copy the contents of one file to another file

source_file = 'sample.txt'
destination_file = 'destination.txt'

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

     

# Q9) Check if a file exists before attempting to read it

import os

file_path = 'sample.txt'

if os.path.exists(file_path):
    print(f"The file {file_path} exists.")
    with open(file_path, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
else:
    print(f"The file {file_path} does not exist.")

     


#  Q10) Delete a file using Python

import os

file_path = 'sample.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")

     
