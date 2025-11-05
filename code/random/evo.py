start = 2
gas = [1, 2, 3, 4, 5]
# indexes = [range(start, len(gas)) + range(0, start)]
indexes = list(range(start, len(gas))) + list(range(0, start))
print(indexes)