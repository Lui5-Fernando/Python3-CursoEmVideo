p = float(input('Digite o seu peso:'))
a = float(input('Digite a sua altura (em metros):'))
a = a*a
imc = p/a
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está como o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')
