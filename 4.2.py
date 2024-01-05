def userdetails(*args, **kwargs):
    name = args[0] if args else kwargs.get('name', 'Unknown')
    email = kwargs.get('email', 'Unknown')
    age = kwargs.get('age', 'Unknown')

    return name, email, age

def main():
    name_input = input("Enter your name: ")
    email_input = input("Enter your email: ")
    age_input = input("Enter your age: ")

    details = userdetails(name=name_input, email=email_input, age=age_input)
    
    print("\nUser Details:")
    print("Name:", details[0])
    print("Email:", details[1])
    print("Age:", details[2])

if __name__ == "__main__":
    main()