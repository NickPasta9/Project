# CPU_Functions.py
#   This program will use a 1-bit adder two 1-bit binary numbers and a
#   carry input and outputs a 1-bit sum and a carry.


def one_bit_adder(a,b,ci):
   # if (a+b+ci) == 1:
   #     sum1 = 1
   #     co = 0
   #     print('sum: ', sum1,
   #           '\nco: ', co)
   # elif(a+b+ci) == 2:
   #     sum1 = 0
   #     co = 1
   #     print('sum: ', sum1,
   #     '\nco: ', co)
   # elif(a+b+ci) == 3:
   #     sum1 = 1
   #     co = 1
   #     print*'sum: ', sum1,
   #     '\nco: ' co)
   # else:
   #     sum1 = 0
   #     co = 0
   #     print('sum: ', sum1,
   #     '\nco: ', co)
    xor_t = xor_g(a,b)
    s = xor_g(xor_t,ci)
    and_1 = and_g(xor_t,ci)
    and_2 = and_g(a,b)
    co = or_g(and_1,and_2)
    return s,co

def main():
    a = int(input("Enter a 1 bit binary number either 0 or 1: "))
    b = int(input("Enter another 1 bit binary number either 0 or 1: "))
    ci = int(input("Enter a carry number either 0 or 1: "))
    (one_bit_adder(a,b,ci))

main()
