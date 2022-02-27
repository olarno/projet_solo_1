import sys 
_, a = sys.argv

a = a.replace(',', '.')
if a.count('.') in [0,1] and a.replace('.', '').isdigit() : 
  a = float()

if not type(a) == float : 
  print('echec')


if opérande1 .isdigit()