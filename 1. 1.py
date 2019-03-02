#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.


input_array = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 6, 28, 7, 29, 2, 3, 12, 13, 14, 14.5, 14.5]
k = 29
answer = 0
m = 0
checked_array = []
i = 0

def recursive_func(num):
    print ("THE NUMBER BEING USED: " + str(num))
    global i
    print ("RECURSIVE FUNCTION WAS ACTIVATED")
    while i < len(checked_array):
            if num + checked_array[i] == k:
                i += 1
                print ("found a pair")
                print ("I EQUALS: " + str(i))
                print ("ANSWER:" + str(int(answer)))
                recursive_func(checked_array[i])
                break
            else:
                i += 1
                print ("new number but not a pair")
                print ("I EQUALS: " + str(i))
                print ("***** 2 THE NUMBER BEING USED: " + str(num))
                recursive_func(checked_array[i])
                break

def func(num):
    if (num) in checked_array:
        print ("number was in checked array")
        print (num)
        recursive_func(num)
    else:
        checked_array.append(num)
        print ("number wasn't in checked array")
        print (num)
        print ("CHECKED ARRAY: " + str(checked_array))


while m < len(input_array):
    func(input_array[m])
    m += 1
    print ("M: " + str(m))



print ("INPUT: " + str(input_array))
print ("K: " + str(k))
print ("CHECKED ARRAY: " + str(checked_array))
print ("ANSWER:" + str(int(answer)))
print ("M: " + str(m))
print ("Length of input array: " + str(len(input_array)))
print ("Length of checked array: " + str(len(checked_array)))
