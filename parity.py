def main():
    x = int(input("What's x? "))
    parity(x)

def parity(n):
    if x % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")

"""
#Same thing with a Return Bool Function

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

    # another ways to do it
    
    return n % 2 == 0
"""


main()