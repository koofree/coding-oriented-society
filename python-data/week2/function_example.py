from __future__ import print_function

# if, for, range, break|continue|else, function,

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))


# function example
def greet(_name):
    print('Hello', _name)


greet('Jack')
greet('Jill')
greet('Bob')
