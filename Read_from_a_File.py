# Open the file in read mode and display its content

file = open("sample.txt", "r")   # "r" = read mode
content = file.read()            # reads the whole file into one string
print(content)
file.close()