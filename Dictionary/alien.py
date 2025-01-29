alien_0 = {'color': 'green', 'point' : 5}
print(alien_0['color'])
print(alien_0['point'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
del alien_0['point']
print(alien_0)

# alien_0 = {'x_position': 0,'speed': 'medium'}
#
# if alien_0['speed'] == 'slow':
#     alien_0['x_position'] += 1
#     print(f'This alien is moving at a {alien_0['speed']} speed!')
# elif alien_0['speed'] == 'medium':
#     alien_0['x_position'] += 2
#     print(f'This alien is moving at a {alien_0['speed']} speed!')
# else:
#     print("This alien is super fast!")