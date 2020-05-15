from sys import argv

print("Type the filename:")
file = input(">")

txt = open(file)

print(txt.read())