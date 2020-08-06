# %%
# Nested Lists - Hackerrank
#%%
# Solution Hackerrank
if __name__ == '__main__':
    lstStudent = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lstStudent.append([name,score])

    second_lowest  = sorted(list(set(([el[1] for el in lstStudent]))), key=float)[1]
    lstResult = sorted([el[0] for el in lstStudent if el[1] == second_lowest])
    [print(el) for el in lstResult]

# %%
# Solution Develop
# %%
# La idea del ejercicio, 
# es crear una lista 
# con los nombres de los estudiantes que tengan la segunda menor nota
# 
# Para efectos practicos, 
# se crea una lista con los datos que se deben ingresar por teclado
some_list = [ ['Harry', 37.21]
			, ['Berry', 37.21]
			, ['Tina', 37.2]
			, ['Akriti', 41]
			, ['Harsh', 39]]

# Dividi el problema en basicamente 3 partes
#
# 1.    Obtener la segunda menor nota
second_lowest  = sorted(list(set(([el[1] for el in some_list]))), key=float)[1]

# 1.1.  Obtener la lista de las notas                                    	# ([el[1] for el in some_list])
# 1.2.  A esa lista quitarle los duplicados                              	# list(set( ... ))
# 1.3.  Ordenar la lista resultado del paso anterior                     	# sorted( ... , key=float)
# 1.4.  Obtener el valor de la segunda posicion, la segunda menor nota   	# .. [1] 
#	
# 2.    Obtener el nombre de los estudiantes con la segunda menor nota	
lstResult = sorted([el[0] for el in some_list if el[1] == second_lowest])	
	
# 2.1.  Obtener la lista                                                 	
#       de los nombres de los estudiantes 
#       que su nota coincida con la segunda menor nota                      # [el[0] for el in some_list if el[1] == second_lowest]
# 2.2.  Ordenar el resultado de la lista anterior                           # sorted( ... ) 
# 
# 3.    Imprimir el resultado
[print(el) for el in lstResult]
# 3.1.  Recorrer la lista resultado del paso anterior
# 3.2.  Imprimir cada elemento de la lista                                  # [print(el) for el in lstResult]

# Notas
# Forma compacta de crear un for
# [el[1] for el in some_list]
# es lo mismo que 
'''
some_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
result_list = []
for el in some_list:
    result_list.append(el[1])
result_list
'''

# %%
