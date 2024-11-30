n = 0
s = 0
m = float('inf')
a = 0

while True:
	x = int(input("Enter a number:"))
	if x == -1:
		break
	n += 1
	s += x
	if x < m:
		m = x

if n > 0:
	a = s / n
else:
	m = -1
	a = -1

print(n,s,m,a)   
