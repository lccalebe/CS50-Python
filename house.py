def main():
    name = input("What's your name? ")
    house(name)

# Use of MATCH
def house(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()