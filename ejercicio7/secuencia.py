a=int(input("ingrese un numero: "))
cant=1
con=1
while cant<=a:
	while con<=cant:
		print cant,
		con=con+1
	print" "
	cant=cant+1
	con=1
cant=a-1
while a >=1:
	while con<=cant:
		print cant,
		con=con+1
	print" "
	cant=cant-1
	con=1
	a=a-1