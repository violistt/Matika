print("Computing the number of quadrant in which degree N is placed in O(1) time")
print()
n = int(input("Enter the number of the degree: "))
print("Number", n, "is in quadrant no.", ((n % 360) // 90) + 1)
