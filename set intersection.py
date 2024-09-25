setx = { "green", "blue"}
sety = {"blue", "yellow"}

print("Original set elements:")
print(setx)
print(sety)

print('\nIntersection of two said sets:')
setz= setx.intersection(sety)
print(setz)

print("\nUnion of two said sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two said sets:")
setz = setz.difference(sety)
print(setz)

print("\nSymnetric difference of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)