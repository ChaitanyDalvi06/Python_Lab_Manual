mylist = input("Enter elements of the list: ").split()

print("List in reverse order using Reverse method:")
for item in reversed(mylist):
    print(item, end=" ")

print()

print("List in reverse order using Slicing:")
for item in mylist[::-1]:
    print(item, end=" ")