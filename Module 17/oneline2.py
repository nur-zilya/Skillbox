s = input()
print(list(filter(lambda x: not (x.isupper() or x.isdigit()), s)))