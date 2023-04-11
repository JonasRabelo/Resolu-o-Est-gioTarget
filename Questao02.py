numA, numB = 0, 1
fib = 0
seq = []

#Número a verificar se está na sequência
number = 54

while number > fib:
	fib = numA + numB
	numA = numB
	numB = fib
	seq.append(fib)




if number in seq:
	print('O número informado pertence a sequência de Fibonacci')
else:
	print('O número informado não pertence a sequência de Fibonacci')