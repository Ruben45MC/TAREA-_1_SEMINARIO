numeros=0
letras=0
cad=raw_input("introduzca la frase: ")
for a in range (len(cad)):
	valor=ord(cad[a])
	if (valor>=48 and valor <=57):
		numeros +=1
	else:
		if (valor >=65 and valor <=90):
			letras +=1
		else:
			if (valor >=97 and valor<=122):
				letras +=1
print ("Letras: "+str(letras))
print ("Digitos: "+str(numeros))
#a='6'
#d=ord(a)
#print d