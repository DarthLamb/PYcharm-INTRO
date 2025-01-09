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
print(f"This is the popped motorcycle: {popped_motorcycle}")
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(f"This is the last motorcycle in the list: {motorcycles}, and this is the one I just removed "
      f":{too_expensive}")
