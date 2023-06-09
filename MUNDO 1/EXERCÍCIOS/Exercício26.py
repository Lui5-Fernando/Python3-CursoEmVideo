f = str(input('Digite uma frase qualquer:')).strip().upper()
print( 'Quantos A aparecem:', f.count('A') )
print( 'Qual o local da primera aparição de A:',f.find('A')+ 1 )
print( 'Qual o local da última aparição de A:',f.rfind('A')+ 1)
