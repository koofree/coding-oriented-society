from __future__ import print_function

'''
Command-line input example
written by Koo(yongku84@gmail.com)
'''


def print_name(_name):
    print('Set value of the variable "name" to %s' % _name)


def print_age(_age):
    print('I am %s years old.' % _age)


# Initial variable of "name"
name = 'koo'
print_name(name)

# Taking input string using command line input
# usage of "input" function
name = input('What is your name?\n')
print_name(name)

old = input('How old are you?\n')
print_age(old)
