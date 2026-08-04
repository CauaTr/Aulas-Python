#Frase inicial
frase = "Aprendendo fatiamento de strings"

print(frase[1:-1])
print(frase[11:21])
print(frase[-1:0:-1])
print(frase[2::3])

import os
os.system("clear")

#Resposta
frase = "Aprendendo fatiamento de Strings"

# 1 - Sem o primeiro e o último

print(frase[2:-1])

# 2 - Somente a palavra fatiamento

print(frase[11:-11])

# 3 - Toda a frase ao contrário

print(frase[::-1])

# 4 - Como executar

print(frase[2::3])