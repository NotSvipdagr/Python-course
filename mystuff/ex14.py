from sys import argv

script, user_name, user_surname = argv
prompt = '==>'

print ("Hi %s %s, i'm the %s script." % (user_name, user_surname, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s %s" % (user_name, user_surname))
likes = input(prompt)

print ("Where do you live %s %s?" % (user_name, user_surname))
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print("Where do you work ?")
work = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer, nice.
And you work at %r, cool dude.
"""% (likes, lives, computer, work)) 