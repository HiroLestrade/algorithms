a = [10,5,7,9,1,2,8,4,6,3]
n = len(a)
k = int((n/2 - 1, n/2)[n%2 != 0]) #índiceBuscado #media

l = 0 #pivoteIzquierdo
m = n-1 #pivoteDerecho
while(l < m):
    x = a[k] #valorEncontrado
    i = l #índiceIzquierdo
    j = m #índiceDerecho
		
		#Mientras los pivotes no se crucen
    while(i <= j):
        while a[i] < x: i+=1 #Buscar en la izquierda un número de derecha
        while a[j] > x: j-=1 #Buscar en la derecha un número de izquierda
        if(i<=j):
						#Intercambiar números
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
						#Desplazar índices
            i+=1
            j-=1
		#Sí el índiceDerecho cruzó al índiceBuscado, 
		#el índiceIzquierdo es un nuevo pivote.
    if j<k: l = i
		#Sí el índiceIzquierdo cruzó al índiceBuscado, 
		#el índicDerecho es un nuevo pivote.
    if k<i: m = j
print(a[k])