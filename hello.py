"""
# Asking user for their name, Remove whitespace from str and Capitalize user's name

name = input("What is your name? ").strip().title()

# Split user's name into firt name and last name

first, last = name.split(" ")

# Say hello to user

print(f"hello, {first}")

"""
def main():
    hello()
    name = input("What's ur name? ").strip().title()
    hello(name)


def hello(name="world"):
    print(f"hello, {name}!")


main()