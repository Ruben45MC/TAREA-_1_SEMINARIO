def es_palindromo(cad):
	cad1=cad[::-1]
	if cad==cad1:
		return True
	else:
		return False
print es_palindromo(raw_input("introduzca una palabra "))
