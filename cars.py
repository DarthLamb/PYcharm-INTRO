cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)
print(f"\nHere is a temporary sort: {sorted(cars)}")
print(f"\nHere is the original: {cars}")
cars.reverse()
print(f"\nHere is the list but reversed: {cars}")
len(cars)