from random import randint
computador = randint(0, 5)
print('_'*90,'\n')

entrada = int(input('Digite um número entre 0 e 5: '))
print('_'*90,'\n')

if computador == 0 and entrada == 0:
    print('VOCÊ VENCEU!')
elif computador == 1 and entrada == 1:
    print('VOCÊ VENCEU!')
elif computador == 2 and entrada == 2:
    print('VOCÊ VENCEU!')
elif computador == 3 and entrada == 3:
    print('VOCÊ VENCEU!')
elif computador == 4 and entrada == 4:
    print('VOCÊ VENCEU!')
elif computador == 5 and entrada == 5:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')