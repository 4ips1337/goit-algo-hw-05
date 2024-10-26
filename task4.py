
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    return inner



contacts = {}


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact {name} updated with phone {phone}."


@input_error
def get_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}'s phone is {contacts[name]}."


@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts available."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()



def handler(command, args):
    if command == "add":
        return add_contact(args, contacts)
    elif command == "change":
        return change_contact(args, contacts)
    elif command == "phone":
        return get_phone(args, contacts)
    elif command == "show all":
        return show_all(args, contacts)
    else:
        return "Unknown command."



def main():
    print("Assistant Bot: How can I help you?")
    while True:
        user_input = input(">>> ").lower()
        if user_input in ["exit", "close", "good bye"]:
            print("Good bye!")
            break

        
        parts = user_input.split()
        if len(parts) < 1:
            print("Enter a command.")
            continue

        command = parts[0]
        args = parts[1:]

        
        response = handler(command, args)
        print(response)


if __name__ == "__main__":
    main()