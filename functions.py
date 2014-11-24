# These functions should be imported to Python through
# the DataNitro plugin: http://datanitro.com/

import Levenshtein

def RFIND(cell, string, beg, end):
    return cell.rfind(string, int(beg), int(end))
 
# It calculates the Levenshtein distance between two strings
def LEV(string1, string2):
    return Levenshtein.distance(string1, string2)

# Function to convert a list of lists where the length of the
# inner lists is always one into a simple list
def flatten(cit_list):
    elements = []
    for el in cit_list:
        elements.append(el[0])
    return elements    
    
# It calculates the h index of a given range of integers (citations)
def HINDEX(elements):
    i = 1 # Counter variable
    # cit_list is a list of lists, where each number is a list of one element.
    # elements is a list of numbers
    if type(elements) is list:
        elements = flatten(elements) 
        # Sorts the list
        elements = sorted(elements, key=int, reverse=True)
        # Iterates through the list until i (counter variable)
        # is higher than citations, and when that happens,
        # it returns the i-1
        for el in elements:
            if el >= i:
                i += 1
            else:
                break
        h_index = i - 1   
    elif elements > 0:
        h_index = 1
    else:
        h_index = 0 
 
    return h_index

# Calculates the Gini index of a list of elements    
def GINI(elements):
    # Checks if the input is a simple list or a list of lists.
    # If it is a list of lists, it flattens it.
    if type(elements[0]) is list:
        elements = flatten(elements)
    # Sorts elements from smallest to largest.
    elements.sort()
    # Counts the number of elements in the list.
    n = len(elements)
    # Calculates the percentage that one element represents in the list.
    hundredth = 100.0 / n / 100
    # Sums the values of all elements in the list.
    total = sum(elements)

    # Creates a list representing the values for perfect equality.
    #hund_eq_list = [hundredth]
    #while int(hund_eq_list[len(hund_eq_list)-1]) != 1:
    #    hund_eq_list.append(hund_eq_list[len(hund_eq_list)-1] + hundredth)

    # Creates a list containing the percentages that the value of each
    # element represent respect to the "total" variable.
    hund_obs_list = []
    for i in elements:
        hund_obs_list.append(i/total)

    # Creates a list containing the accumulated values of "hund_obs_list"    
    hund_obs_list_acc = []
    sum_obs = 0
    for j in hund_obs_list:
        sum_obs += j
        hund_obs_list_acc.append(sum_obs)

    # Calculates the points that form the Lorenz curve
    area_b_list = []
    prev_hund_obs = 0
    for hund_obs_el in hund_obs_list_acc:
        b_point = ((hund_obs_el + prev_hund_obs) / 2.0) * hundredth
        area_b_list.append(b_point)
        prev_hund_obs = hund_obs_el

    # Calculates the percentage of the area below the line of perfect
    # equality that is also above the Lorenz curve --> Gini index
    sum_b = sum(area_b_list)
    area_a = 0.5 - sum_b
    gini = area_a / 0.5
    
    return gini
    
    
    
    

