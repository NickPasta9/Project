# Logic_Gates.py
#   This program consists of inputs and outputs used to display a binary
#   number (0 or 1) based on the given value through logic gates

def and_g(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return 1

def or_g(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def not_g(a):
    if a == 1:
        return 0
    else:
        return 1

def nand_g(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def xor_g(a,b):
    if(a == 0 and b == 0) or (a == 1 and b == 1):
        return 0
    else:
        return 1

def main():
    a = int(input("Enter a number either 0 or 1: "))
    b = int(input("Enter a number either 0 or 1: "))
    print("And: ", and_g(a,b))
    print("Or: ", not_g(a))
    print("Not: " not_g(a))
    print("Nand: ", nand_g(a,b))
    print("Xor: ", xor_g(a,b))

main()
