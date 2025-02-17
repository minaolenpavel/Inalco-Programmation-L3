from utils_listes import premier_dernier, meme_longueur
from utils_dict import meme_cles
from utils_comparaison import egalite

l1 = [1, 4, 19, 0]
premier_dernier(l1) # affiche le premier et le dernier élément de la liste séparés par une tabulation
l2 = [3, 0, 8]
l3 = [2, 2, -1, 3]

meme_longueur(l1, l2) # affiche 'même longueur' si les listes ont le même nombre d'éléments, 'pas la même longueur' sinon
meme_longueur(l1, l3) # //

d1 = {
  'telephone': '0123456789',
  'adresse': "2 rue Victor Hugo",
  'code postal': '08465'
}

d2 = {
  'telephone': '0143458789',
  'adresse': "2 avenue de la République",
  'code postal': '08465'
}

d3 = {
  'telephone': '0340258789',
  'adresse postale': "11 rue de l'Hôpital",
  'code postal': '08465'
}

meme_cles(d1, d2) # affiche 'mêmes clés' si les dictionnaires ont les mêmes clés, 'pas les mêmes clés sinon'
meme_cles(d1, d3) # //

print(egalite([d1["code postal"], d2["code postal"], d3["code postal"]])) # renvoie True si tous les éléments de la liste sont identiques, False sinon 
print(egalite([d1["telephone"], d2["telephone"], d3["telephone"]])) # //
