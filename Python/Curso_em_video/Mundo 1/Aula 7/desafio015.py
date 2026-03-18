d=float(input('Por quanto tempo o veículo foi alugado?'))
km=float(input('Quantos Km foram rodados com o veículo em questão?'))

print('A diária do veículo resultará no valor de {:.2f} reais somados a {} por uso pessoal.'.format((d*60),(km*0.15)))
print('portanto o valor total a ser pago será de {:.2f} reais'.format((d*60+km*0.15)))