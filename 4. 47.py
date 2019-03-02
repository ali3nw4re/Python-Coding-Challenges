# Given a array of numbers representing the stock prices of a company in
# chronological order, write a function that calculates the maximum profit you
# could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
# buy the stock at 5 dollars and sell it at 10 dollars.


inputArray = [8, 29, 5, 10, 13, 2]
smallArray = [10]
smallestNumber = 0

# length = len(inputArray)
# smallLength = len(smallArray)

for i in inputArray:
    if len(smallArray) > 0:
        for j in smallArray:
            if inputArray[i] < smallArray[j]:
                smallestNumber = inputArray[i]
                print (smallestNumber)
                madeByMinuk = input("inputArray was smaller than smallArray")
            else:
                smallArray.append(inputArray[i])
                madeByMinuk = input("number was added to the small array")
    else:
        smallArray.append(inputArray[i])

print ("input array: " + str(inputArray))
print ("small array: " + str(smallArray))

madeByMinuk = input("Press enter to exit")
