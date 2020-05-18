#déclaration de variable 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# print des variables x y
print(x)
print(y)

# repeat des variables 
print("I said: %r." % x)
print("I also said: '%s'." % y) 

#déclarations des variables hilarious and joke
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#%r = raw data just for debugging
print(joke_evaluation % hilarious)

#déclaration des variables
w= "This is the left side of..."
e= "a string with a right side."
# affichage de w + e = "this is the ...... right side." 
print(w + e)

