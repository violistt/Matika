import math
from fractions import Fraction


def arc_lenght_to_degrees(quotator, denominator):
    return math.ceil(((quotator / denominator) * math.pi) * (180 / math.pi))

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def degrees_to_arc_lenght(degrees, radius):
    ans = Fraction((degrees * (math.pi / 180) * radius) / math.pi)
    if (not ans % 1):
        return 1
    else:
        res = str(ans)
        pos = res.index('/')
        quotator = int(res[:pos])
        denominator = int(res[pos + 1:])
        gcd_ = gcd(quotator, denominator)
        quotator //= gcd_
        denominator //= gcd_
        ans = quotator / denominator
        return Fraction(ans).limit_denominator(1000)

def solve():
    choice = int(input("Arc lenght to degrees: (0), degrees to arc lenght: (1): "))
    if (choice == 0):
        print()
        print("Converting arc lenght to degrees")
        print()
        quotator, fraction, denominator = input("Enter fraction number with spaces after every character (3 / 4): ").split()
        quotator = int(quotator)
        denominator = int(denominator)
        print(quotator, "/", denominator, "π", "is equal to", arc_lenght_to_degrees(quotator, denominator), "°")
    elif (choice == 1):
        print()
        print("Converting degrees to arc lenght")
        print()
        degrees = int(input("Enter the number of degrees: "))
        radius = int(input("Enter the radius of the circle: "))
        print(degrees, "°", "is equal to", degrees_to_arc_lenght(degrees, radius), "π", "in arc lenght")
    else:
        print("Invalid input, please try again")

def main():
    return solve()

main()
