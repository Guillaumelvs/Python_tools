"""
Created on Fri Oct 29 09:13:57 2021

@author: Guillaumelvs

Suppression des commentaires d'un code SAS
"""


import re 

the_code ='''
Put your SAS code here
'''


def remove_com(the_code):    
    all_index_to_remove =[]
    pattern = re.compile(r';[\n \t]+\*')
    matches = pattern.finditer(the_code)
    
    for m in matches:
        beginning = m.end() -1
        temp_pattern = re.compile(r';')
        temp_matches = temp_pattern.finditer(the_code[beginning:])
        temp_all_find = []
        for m_temp in temp_matches:
            temp_all_find.append(m_temp.start())
        end = temp_all_find[0] + 1 + beginning
        all_index_to_remove.append(beginning)
        all_index_to_remove.append(end)
        
        
        
    #Traitement à part du cas où le commentaire est collé au ; de l'instruction precedente    
        
    pattern2 = re.compile(r';\*')
    matches2 = pattern2.finditer(the_code)
    
    for m in matches2:
        beginning = m.end() - 1
        temp_pattern = re.compile(r';')
        temp_matches = temp_pattern.finditer(the_code[beginning:])
        temp_all_find = []
        for m_temp in temp_matches:
            temp_all_find.append(m_temp.start())
        end = temp_all_find[0] + 1 + beginning
        all_index_to_remove.append(beginning)
        all_index_to_remove.append(end)   
        
    pattern3 = re.compile(r'/\*')
    matches3 = pattern3.finditer(the_code)
    
    for m in matches3:
        beginning = m.end() - 2
        temp_pattern = re.compile(r'\*/')
        temp_matches = temp_pattern.finditer(the_code[beginning:])
        temp_all_find = []
        for m_temp in temp_matches:
            temp_all_find.append(m_temp.start())
        end = temp_all_find[0] + 2 + beginning
        all_index_to_remove.append(beginning)
        all_index_to_remove.append(end)
    
    all_index_to_remove.sort()
    nb_of_element_to_remove = int(len(all_index_to_remove)/2) 
    nb_of_removed_element = 0
    
    for i in range(nb_of_element_to_remove):
        first_index = all_index_to_remove[2 * i] - nb_of_removed_element
        end_index = all_index_to_remove[(2 * i) + 1] - nb_of_removed_element
        the_code = the_code[0:first_index] + the_code[end_index:]
        nb_of_removed_element += end_index - first_index
        
    return the_code   
        
print(remove_com(the_code))    #If the string is too long you can export it in a .txt file