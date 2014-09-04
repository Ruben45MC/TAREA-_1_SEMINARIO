print("a)")
for i in range(20):
	print (i+1),
print(" ")
print("b)")
a=20
for j in range(20):
	print a,
	a-=1
print(" ")
print("c)")
def suma(a,b):
	x=int(a)
	y=int(b)
	v=x+y
	return v
print suma(raw_input(),raw_input())
print(" ")
print("d)")


def suma2(c,d):
	o=str(c)
	p=str(d)
	n=o+p
	return n

print suma2(int(input()),int(input()))
print("e)")

def suma3(entero,flo):
	return entero+flo

print suma3(int(input()),float(input()))