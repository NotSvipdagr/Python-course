#import argv module
from sys import argv

script, filename = argv
#Open file ext15_sample.txt
txt = open(filename)

print("Here's your file %r:" % filename)
#print le contenue du file via la variable txt
print(txt.read())
#demande à l'utilisateur d'entrer le nom du fichier txt
print("Type the filename again:")
file_again = input(">")
#ouvre le fichier renseigner par le user
txt_again = open(file_again)

print(txt_again.read())

close(txt, txt_again)