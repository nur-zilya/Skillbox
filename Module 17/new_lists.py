from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

floats_cubes = list(map(lambda x:  round(x ** 3, 2), floats))
new_names = list(filter(lambda x: len(set(x)) >= 5, names))
numbers_prod = reduce(lambda x, y: x*y, numbers)


print(floats_cubes, new_names, numbers_prod)