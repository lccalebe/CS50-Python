def main():
    x = int(input("Pet the cat how many times? "))
    while x <= 0:
        x = int(input("Plese type a posive number.\nPet the cat how many times? "))

    print("Meow\n" * x, end = "")

    #meow(x)
    #meow2(x)

# Use of WHILE
def meow(n):    
    
    while n != 0:
        print("Meow")
        n -= 1
    
    """
    i = 0
    while i < n:
        print("Meow")
        i += 1
    """

# Use of FOR
def meow2(n):
    for _ in range(n):
        print("Meow")

main()