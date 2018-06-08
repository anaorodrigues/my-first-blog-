#comentario

#definir funcoes antes de chamar
def hi(nome):
  if nome=='Ana':
    print('oi ana')
  elif nome == 'Lu':
    print('oi lu')
  else:
    print('quem e vc??')

print('hello djangogirls')

if 3>4:
  print('works')
else:
  print('erro')

hi('Ana')

girls = ['Ana', 'Bia', 'Dani']
for name in girls:
  print('Oi '+name+'.')

#Atencao: range(x,y) vai ate y-1!!
for i in range(1,6):
  print(i)

