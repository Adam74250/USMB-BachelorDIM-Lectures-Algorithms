"""
Session 1
@author : Adam MACHEDA, LP Dim
"""

tab = [2, 4, -1, 0, -1, 2]

# This function computes the average of the positive elements of a table
def algo1(tab):
    if len(tab) == 0 :
        return ValueError('Valeur nulle')
    else :
        Som = 0
        N = 0

        for item in tab:
            if item > 0:
                Som += item
                N += 1
        Moy = float(Som)/float(N)

        return float(Moy)

# This function gets the maximum value of a table
def algo2(tab):
    if len(tab) == 0 :
        return ValueError('Valeur nulle')
    else :
        Max = tab[0]
        for item in tab:
            if item > Max:
                Max = item

        return float(Max)

# This function reverses a table without the use of any other table
def algo3(tab):
    if len(tab) == 0 :
        return ValueError('Valeur nulle')
    else :
        for i in range(len(tab)) :
            if i < len(tab)/2:
                valEnCours = tab[i]
                tab[i] = tab[(len(tab)-i)-1]
                tab[(len(tab)-i)-1] = valEnCours

        return tab

print("{var}".format(var=algo3(tab)))
