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
    print("MODE: + ou - ou * ou /")
    print("+: addition")
    print("-: soustraction")
    print("*: multiplication")
    print("/: divission")
    print("Les arguments suivants OP1 et OP2")
    print("Ces deux, doivent etre des chiffre soit en int() soit en float()")
    print("exemple: 10 34 23.5 13.65")
    print("Exemple d'utilisation: python calculate.py + 10 24.5")
  else :
    print("Pour plus d'informations, éxecutez : python calculate.py aide")
elif len(sys.argv) != 4:
  print("Mauvais nombre d'arguments.")
  print("Pour plus d'informations, éxecutez : python calculate.py aide")
else:
  _, mode, op1, op2 = sys.argv
  print(type(mode), mode)
  print(type(op1), op1)
  print(type(op2), op2)
  exit()


# 1.a.3 Sinon on continue
# 2. Vérifier les valeurs des arguments :
# 2.a MODE : doit être compris entre + - * / 
# 2.b OP1 : doit être soit un float() soit un int()
# 2.c OP2 : doit être soit un float() soit un int()

## Execution de la calulatrice 
# En fonction du MODE 

# + : OP1 + OP2 
# Afficher le résultat 

# - : OP1 - OP2
# Afficher le résultat

# * : OP1 * OP2 
# Afficher le résultat 

# / : OP1 / OP2 
# Afficher le résultat 

