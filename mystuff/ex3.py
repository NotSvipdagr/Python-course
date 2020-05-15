#Affiche I will now count my chickens
print ("I will now count my chickens:")
#additionne 25 avec 30 divisé par 6 (= 5)
print ("Hens", float(25 + 30 / 6))
#on multiplie 25 par 3 = 75 et on prend le modulus (le reste de la division) de 75 % 4 = 3, 
#que l'on soustrait à 100
print ("Roosters", float(100 - 25 * 3 % 4))

print ("Now I will count the eggs:")
#modulo de 4/2 et division de 1/4 et ensuite addition du reste
print (float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

print("Is it true that 3 + 2 < 5 - 7?")
#Est-ce que 5 est plus petit que -2 = False
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)

print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")
#Est ce que 5 est plus grand que -2 = True
print("Is it greater?", 5 > -2)
#Est ce que 5 est plus grand ou egal à -2 = True
print("Is it greater or equal?", 5 >= -2)
#ESt ce que 5 est plus petit ou égal à -2 = False
print("Is it less or equal?", 5 <= -2)
