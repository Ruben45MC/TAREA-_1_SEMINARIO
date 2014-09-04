def primo(num):
	res=0
	a=1
	n=2
	con=0
	b=1
	while a<=num:
		con=0
		b=1
		while b<=n:
			if n%b==0:
				con +=1
			b +=1
		if con==2:
			res=res+n
			a +=1
		n +=1
	return res

print primo(int(input("introduzca la cantidad de numeros para sumar: ")))