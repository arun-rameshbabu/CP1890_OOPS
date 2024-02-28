
def title():
    print("SALES DATA IMPORTER\n")


def command_menu():
    print("COMMAND MENU")
    print("view - View all sales")
    print("add - Add sales")
    print("import - Import sales from file")
    print("menu - Show menu")
    print("exit - Exit program")


def main():
    title()
    command_menu()
    while True:
        option = input("\nPlease enter a command: ")
        if option == "view":
            print("View all sales")
        elif option == "add":
            print("Add sales")
        elif option == "import":
            print("import sales from file")
        elif option == "menu":
            print("Show menu")
        elif option == "exit":
            print("\nBye!")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
