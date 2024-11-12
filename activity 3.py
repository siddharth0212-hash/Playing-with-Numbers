# Program to find HCF/GCD

#Using Eucliden Algorithms
def hcf(numberSmallest,numberLargest):
    while(numberSmallest):
        numberStore = numberSmallest
        numberSmallest = numberLargest % numberSmallest
        numberLargest = numberStore
    return numberLargest

#Enter 2 numbers
numberLargest = int(input("Enter Largest Number :  "))
numberSmallest = int(input("Enter Smallest number : "))


# LCM equals product of number divide hcf of the numbers
lcm = int((numberSmallest / hcf(numberSmallest,numberLargest))* numberLargest )
print("LCM is : ",lcm)