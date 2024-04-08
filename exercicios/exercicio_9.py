#Faça um algoritmo que leia um valor em metros e converta para centímetros e milímetros
metros = float(input('Digite o valor em metros: '))
cm = metros * 100
mm = metros * 1000

print('{} metros em centímetros vale {} e em milímentros vale {}'.format(metros, cm, mm))
