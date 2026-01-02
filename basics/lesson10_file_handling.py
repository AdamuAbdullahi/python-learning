# open the file in a read mode
file = open("example.txt", "r")

# Read the content
content = file.read()
print("File Content:/n", content)

# Close the file
file.close()