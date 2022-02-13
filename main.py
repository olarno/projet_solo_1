# 1. récupere les arguments 
import sys
## Vérification d'usage 
#argv = main.py mode ope1 ope2
#argv = main.py aide
# 1.a compter les arguments 
# 1.a.1 Si 1 et == aide -> Afficher l'aide 
# 1.a.2 Si different de 3 (mode ope1 ope2) afficher message d'erreur et explication 
if len(sys.argv) == 2:
  _, command = sys.argv
  if command == "aide":
    print("Aide a l'utilisation de la calculatePy.")
    print("Tout ce passe en ligen de commande, voici commnent l'utiliser au mieux")
    print("Faire appel au script : python calculate.py MODE OP1 OP2")
    print("Les différentes possibilités pour les arguments")
    print("MODE: + ou - ou x ou /")
    print("+: addition")
    print("-: soustraction")
    print("x: multiplication")
    print("/: divission")
    print("Les arguments suivants OP1 et OP2")
    print("Ces deux, doivent etre des chiffre soit en int() soit en float()")
    print("exemple: 10 34 23.5 13.65")
    print("Exemple d'utilisation: python calculate.py + 10 24.5")
    exit()
  else :
    print("Pour plus d'informations, éxecutez : python calculate.py aide")
    exit()
elif len(sys.argv) != 4:
  print("Mauvais nombre d'arguments.")
  print("Pour plus d'informations, éxecutez : python calculate.py aide")
  exit()
else:
  # 1.a.3 Sinon on continue
  # 2. Vérifier les valeurs des arguments :
  # 2.a MODE : doit être compris entre + - * / 
  _, mode, op1, op2 = sys.argv
  operateurs = ['+', '-', 'x', '/']
  # 2.b OP1 : doit être soit un float() soit un int()
  # 2.c OP2 : doit être soit un float() soit un int()
  if '.' in op1:
    op1 = float(op1)
  else:
    op1 = int(op1)
 
  if '.' in op2:
    op2 = float(op2)
  else:
    op2 = int(op2)


  ## Execution de la calulatrice 
  # En fonction du MODE 
  if mode in operateurs:
    if mode == '+':
      # + : OP1 + OP2 
      # Afficher le résultat 
      res = op1 + op2
      print(f"Résultat de l'addition : {op1} {mode} {op2} = {res}")
    elif mode =='-':
      # - : OP1 - OP2
      # Afficher le résultat
      res = op1 - op2
      print(f"Résultat de la soustraction : {op1} {mode} {op2} = {res}")
    elif mode == 'x':
      # * : OP1 * OP2 
      # Afficher le résultat
      res = op1 * op2
      print(f"Résultat de la multiplication : {op1} {mode} {op2} = {res}")
    else : # /
      # / : OP1 / OP2 
      # Afficher le résultat 
      res = op1 / op2
      print(f"Résultat de la division : {op1} {mode} {op2} = {res}")
  else: 
    print("Mauvais arguments.")
    print("Pour plus d'informations, éxecutez : python calculate.py aide")
    exit()