import sys
############################
# Extraction des Arguments #
############################

nom_script, *arguments = sys.argv

# on vérifie si le mode est supporté
modes = ['ajout', 'différence', 'produit', 'ratio', 'puissance']

# défini un message d'aide
aide = f"""Bienvenue dans le pogramme {nom_script}

Pour utiliser ce programme merci de respecter la syntaxe suivante 
► python {nom_script} <mode> <opérande1> <opérande2>

remplacer  <mode> avec l'opération désirée parmis : 
► 'ajout' pour faire une addition
► 'différence' pour faire une soustraction
► 'produit' pour faire une multiplication
► 'ratio' pour faire une division
► 'puissance' pour calculer la puissance d'un nombre 

remplacer <opérande1> et <opérande2> par des nombres entiers ou à virgule.
⟁ merci d'écrire les nombres à virgule avec des points '.' à la place des virgules ','
"""
# afficher un message d'aide si besoin 

# si zéro arguments
if len(arguments) != 3 :
  print(aide)
  exit() 

mode, opérande1, opérande2 = arguments # unpacking
# mettre le mode en min
mode = mode.lower()

if mode == 'aide' :
  print(aide)
  exit()


# si le cas n'est pas supporté affichage d'aide
if mode not in modes : 
  print('Le mode demandé : ', mode, 'n\'est pas supporté.')
  print('Liste des modes supportés : ', modes)
  print('\nPour afficher les instructions merci d\'utiliser la commane suivante :')
  print(f'► python {nom_script} aide')
  exit()


####################################
# Convertir les opérandes en float #
####################################

# remplacer les virgules par des points
op1 = opérande1.replace(',', '.')
# on compte le nombre de points 
# puis on verifie que tout ce qui n'est pas un point est un chiffre 
if op1.count('.') in [0,1] and op1.replace('.', '').isdigit() : 
  op1 = float(op1)
else:
  print('Opérande 1 (recu : ', opérande1, ' n\'a pas pu être convertie en float')
  exit()

op2 = opérande2.replace(',', '.')
if op2.count('.') in [0,1] and op2.replace('.', '').isdigit() : 
  op2 = float(op2)
else:
  print('Opérande 2 (recu : ', opérande2, ' n\'a pas pu être convertie en float')
  exit()

#####################################
# Implémentation de la calculatrice #
#####################################

if mode == modes[0]: # addition
  résultat = op1 + op2
  symbole = '+'
elif mode == modes[1]: # soustraction
  résultat = op1 - op2
  symbole = '-'
elif mode == modes[2]: # multiplication
  résultat = op1 * op2 
  symbole = '*'
elif mode == modes[3]: # division
  résultat = op1 / op2
  symbole = '/'
elif mode == modes[4]: # puissance
  résultat = pow(op1, op2)
  symbole = '^'


conclusion = f'Le résultat de {op1} {symbole} {op2} est {résultat}'
print(conclusion)