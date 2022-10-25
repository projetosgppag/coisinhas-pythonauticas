import random

while True:
  lin = int(input("Digite a quantia de linhas da matrix: "))
  col = int(input("Digite a quantia de colunas da  matrix: "))
  if lin > 0 and col > 0:
    matrix = []
    for i in range(lin):
      LINHA = []
      for j in range(col):
        num = random.randint(0,100)
        LINHA.append(num)
      matrix.append(LINHA)
    break
print(matrix)
