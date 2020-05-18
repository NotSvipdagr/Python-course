#Output de la fonction, 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

#définition de cheese_and_crackers avec 20 30 directement
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#définition via des variables
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#appel de la fonction avec les variables amount_of_cheese, amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#définition des variables cheese_count et boxes_of_crackers et addition
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Définition via variables et addition
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +100)

#drill 3

def coca_et_sprite (coca, sprite):
    print("You have %d coca" % coca)
    print("You have %d sprite" % sprite)
    print("That's a lot of beverage")
    print("You're thirsty? \n")

coca_et_sprite(20, 30)

coca = 50
sprite = 60
coca_et_sprite(coca, sprite)

coca = 50 + 50 
sprite = 60 + 60
coca_et_sprite(coca, sprite)

coca_et_sprite(coca + 20, sprite + 20)