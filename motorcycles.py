motorcycles = ['honda', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ramen'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'miyuzuki')
del motorcycles[1]
print(motorcycles)

print("Now I am popping")
popped_motorcycle = motorcycles.pop(0)
print(popped_motorcycle)
