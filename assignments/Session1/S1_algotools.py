"""
Session 1
@author : Adam MACHEDA, LP Dim
"""

tab = [2, 4, -1]

def algo1(tab):
    Som = 0
    N = 0

    for item in tab:
        if item > 0:
            Som += item
            N += 1
    Moy = float(Som)/float(N)

    return float(Moy)

def algo2(tab):
    if len(tab) == 0 :
        return ValueError('Valeur nulle')
    else :
        Max = tab[0]
        for item in tab:
            if item > Max:
                Max = item

        return float(Max)

print("Insertion balistique : {var}".format(var=algo2(tab)))
