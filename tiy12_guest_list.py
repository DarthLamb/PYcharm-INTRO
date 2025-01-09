guest_list = ['Mike', 'Dave', 'Nick']
print(f"Hello {guest_list[0]}!")
print(f"Hey {guest_list[1]}!")
print(f"Nice to see you {guest_list[2]}!")
print(f"It seems that {guest_list[2]} can't make it.")

guest_list.remove('Nick')
guest_list.append('Mitch')

print(f"Hello {guest_list[0]}!")
print(f"Hey {guest_list[1]}!")
print(f"Nice to see you {guest_list[2]}!")
print("\nIt seems I found a bigger table!")
guest_list.insert(0, 'Manny')
guest_list.insert(2, 'Edgar')
guest_list.append('Rick')

print(f"\n{guest_list}")
print(f"Hello {guest_list[0]}!")
print(f"Nice to see you {guest_list[2]}!")
print(f"Hey {guest_list[-1]}!")

print("\nThe new table wont arrive in time so I will have to ask many of you to leave.")

guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(guest_list)
del guest_list[0]
del guest_list[1]
print(guest_list)