from array2D import slice_me


family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("pas une liste")
family = {1, 2, 3}
print(slice_me(family, 0.3, 2))
print(slice_me(family, 1.2, -2))

print("liste vide")
family = []
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("pas un int")
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0.3, 2))
print(slice_me(family, 1.2, -2))

print("pas le meme taille")
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

