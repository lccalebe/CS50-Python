def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    compare(x, y)


def compare(x, y):

    
    # use of IF, ELIF and ELSE
    if x < y:
        print(f"{x} is less than {y}")
    elif x > y:
        print(f"{x} is greter than {y}")
    else:
        print(f"{x} is equal than {y}")
    

    """
    # use of OR
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")
    """

    """
    # use of NOT EQUAL(!=)
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")
    """

main()