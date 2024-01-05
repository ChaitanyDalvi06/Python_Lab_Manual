numbers = [int(n) for n in input("Enter numbers separated by spaces: ").split()]

cubes_tuples = [(num, num ** 3) for num in numbers]

print("List of tuples giving cube for num:", cubes_tuples)