from __future__ import print_function

# coding=utf-8
# Numbers, String, Unicode Strings, Lists

# list
friend_list = ['john', 'pat', 'gary', 'michael']
print('friend list : ' + str(friend_list))
print()
other_friend = 'smith'
other_friend_list = [other_friend]

new_friends = friend_list + other_friend_list
new_friends = friend_list.append(other_friend)

num = 1
end = 3

print(friend_list)
print(friend_list[0], friend_list[2])
print(friend_list[:3])
print(friend_list[num:end])
print()
print(new_friends)
print(friend_list)

friend_list.remove('gary')
print(friend_list)
print(len(friend_list))
print(len('g'))


# for i, name in enumerate(friends):
#    print "iteration {iteration} is {name}".format(iteration=i, name=name)
