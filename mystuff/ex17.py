from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on one line too, how? Yes
indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)
# always close a file open
out_file.close()


# in one line :
#from sys import argv
#open(argv[2], 'w').write(open(argv[1]).read())