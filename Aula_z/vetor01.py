import os
os.system("cls")

#Criando um "vetor"
#    0    1   2   3    4
#    -5  -4  -3  -2   -1
v = [45, 56, 76, -45, 34]

print(v, len(v), type(v))
print(v[0])
print(v[-1])

# for i in range(0, len(v), 1):
#     print(i+1, ':', v[i])

# for i in v:
#   print(i)

for i, c in enumerate(v, 1):
    print(f'{i} - {c}', end=" | ")