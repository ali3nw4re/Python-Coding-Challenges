#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def print_func(string):
    print (string)
    made_by_minuk = input("Press Enter to escape")

func = input("What would you like to print? ")
n = input("How long do you want to wait in milleseconds? ")

n = int(n) / 1000

time.sleep(n)

print_func(func)
