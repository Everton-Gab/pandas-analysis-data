#Exemplos com listas, tuplas, conjuntos, operadores
#Uma lista é uma coleção ordenada e mutável

numeros= [1,2,3]
letras= ['a','b','c']
mistura=[1.0,'a',True]
print("lista de numeros:",numeros)

numeros.append (4)
numeros[0]=99
print("lista alterada:",numeros)

#----Tuplas-----
#Tupla é uma coleção ordenada e imutavél
Tupla=("what","who","Where")
print("Tupla:",Tupla)

#Um set é uma coleção não ordenada e não permite itens duplicados

Frutas= set(['batata', 'Alface', 'Uva', 'Uva']) 
print("set sem duplicados:",Frutas)
Frutas.add("banana")
print("set após add:",Frutas)

#---FrozenSet---
#Este subtipo de PyObject é usado para manter os dados internos para ambos os objetos set e frozenset.
conjunto=frozenset(['batata', 'alface', 'uva'])
print("Frozenset:", conjunto)

#---Operações entre sets-----

a={1,2,3}
b={3,4,5}
print("\n União de a com b:", a|b)
print("Interseção:",a&b)
print("Diferença:",a-b)

#---operadores----
x,y=10,5
print("igual a ", x==y)
print("diferente de", x!=y )
print("maior que", x>y)
print("menor que", x<y)
print("maior ou igual a ", x>=y)
print("menor ou igual a ", x<=y)

#operadores lógicos(booleanos)
p,q=True,False
print("\n p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

#operadores Aritmeticos
print(5+2, 5-2, 5*2, 5/2, 5//2, 5%2, 5**2)