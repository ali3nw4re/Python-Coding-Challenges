#Given a singly linked list and an integer k, remove the kth last element from the list.
#k is guaranteed to be smaller than the length of the list.
longList = [8, 6, 4, 3, 5, 2, 4, 5, 6, 2, 4 ,6]

print (longList)

k = input("What is your K? ")
k = int(k)

removal = len(longList) - k

del longList[removal]


print (longList)
