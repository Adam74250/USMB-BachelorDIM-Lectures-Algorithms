"""
Session 1
@author : Adam MACHEDA, LP Dim
"""

import numpy

tab = [2, 4, -1, 0, -1, 2]
mat = numpy.zeros([7, 8])
mat[1, 3] = 1
mat[2:7, 3:6] = 1
mat[6:7, 3:8] = 1

##
# This function computes the average of the positive elements of a table
def average_above_zero(tab):
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

##
# This function gets the maximum value of a table
def max_value(tab):
    if len(tab) == 0 :
        return ValueError('Valeur nulle')
    else :
        Max = tab[0]
        for item in tab:
            if item > Max:
                Max = item

        return float(Max)

##
# This function reverses a table without the use of any other table
def reverse_table(tab):
    n = len(tab)
    if n == 0 :
        return ValueError('Valeur nulle')
    else :
        for i in range(n) :
            if i < n/2:
                valEnCours = tab[i]
                tab[i] = tab[(n-i)-1]
                tab[(n-i)-1] = valEnCours

        return tab

##
# Selective sorting
def selective_sort(tab):
    n = len(tab)
    for i in range(n):
        kMin = i

        for j in range(i+1, n):
            if tab[j] < tab[kMin]:
                kMin = j

        valEnCours = tab[i]
        tab[i] = tab[kMin]
        tab[kMin] = valEnCours

    return tab

##
# Bubble sorting
def bubble_sort(tab):
    n = len(tab)
    tourEnCours = 0
    traitement = True

    while traitement == True:
        traitement = False
        for i in range (0, n-tourEnCours-1):
            if tab[i] > tab[i+1]:
                valEnCours = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = valEnCours

                traitement = True
        tourEnCours += 1

    return tab

##
# Bounding box
def roi_bbox(mat):
    xmin = mat.shape[0]
    xmax = 0
    ymin = mat.shape[1]
    ymax = 0

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i, j] > 0:
                if xmin > i:
                    xmin = i
                if xmax < i:
                    xmax = i

                if ymin > j:
                    ymin = j
                if ymax < j:
                    ymax = j

    bbox_coords = numpy.zeros([4, 2])
    bbox_coords[0,:] = numpy.array([ymin, xmin])
    bbox_coords[1,:] = numpy.array([ymax, xmin])
    bbox_coords[2,:] = numpy.array([ymin, xmax])
    bbox_coords[3,:] = numpy.array([ymax, xmax])

    return bbox_coords

print(mat)
print("{var}".format(var=roi_bbox(mat)))
