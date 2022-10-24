def calc_primos(x):
    contador = int()
    holder = x
    for x in range(x,0,-1):
        if holder % x == 0:
            contador+=1
    if contador == 2:
        return True
    else:
        return False
#############################################################
l = [y for y in range(0,101) if calc_primos(y) == True]  # lista de todos os primos de 0 a 100
dicto = {f'{y}': f'{calc_primos(y)}' for y in range(0,101)} # dict de todos os primos de 0 a 100
