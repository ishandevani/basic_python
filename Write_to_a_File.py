# Create a text file and write content to it

file = open("sample.txt", "w")          # "w" = write mode (creates fileile ifile missing)
file.write("Hello, DevOps.\n")
file.write("This is python\n")
file.close()                            # must close, or data may not be saved

# Read it back to confirm
file = open("sample.txt", "r")          # "r" = read mode
print(file.read())
file.close()