def ValorCadena(cad1,cad2):
	if len(cad1)>len(cad2):
		return "la palabra mas larga es "+cad1
	else:
		if len(cad2)>len(cad1):
			return "la palabra mas larga es "+cad2
		else:
			return "las dos palabras tienen la misma longitud "+cad1+cad2

print ValorCadena(raw_input("introduzca una palabra: "),raw_input("introduzca otra palabra: "))
