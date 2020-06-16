valor = int(input('Digite um numero:'))
aux = 1
print('='*10)
print('Tabuada {}'.format(valor))
print('='*10)
while (aux <= 10):
	print('{0}x{1}={2}'.format(aux,valor, (aux * valor)))
	aux = aux+1