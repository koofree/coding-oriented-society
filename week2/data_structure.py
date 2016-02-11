# Python interpreter language
# Simple data structures
# List, Tuple, Set, Dictionary

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    if i >= 2:
        print "iteration {iteration} is {name}".format(iteration=i, name=name)
    else:
        print 'No output.'

for i in range(0, 4):
    name = friends[i]
    print "iteration {iteration} is {name}".format(iteration=i, name=name)


for i in range(0, len(friends)):
    name = friends[i]
    print "iteration {iteration} is {name}".format(iteration=i, name=name)


for name in friends:
    print name
