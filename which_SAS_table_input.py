"""
Created on Thu Oct 28 10:06:38 2021

@author: Guillaumelvs

NB : installer au préalable le package openpyxl via "conda install -c anaconda openpyxl"  
"""


import re
import pandas as pd

test_code='''
put your code here.
'''

####################################################################

#Enlever cette partie si on veut aussi extraire les bases appelées dans les commentaires

####################################################################

all_index_to_remove =[]
pattern = re.compile(r';[\n \t]+\*[a-zA-Z0-9.&_ \n\t]')
matches = pattern.finditer(test_code)

for m in matches:
    beginning = m.end() -1
    temp_pattern = re.compile(r';')
    temp_matches = temp_pattern.finditer(test_code[beginning:])
    temp_all_find = []
    for m_temp in temp_matches:
        temp_all_find.append(m_temp.start())
    end = temp_all_find[0] + 1 + beginning
    all_index_to_remove.append(beginning)
    all_index_to_remove.append(end)
    
    
    
#Traitement à part du cas où le commentaire est collé au ; de l'instruction precedente    
    
pattern2 = re.compile(r';\*[a-zA-Z0-9.&_ \n\t]')
matches2 = pattern2.finditer(test_code)

for m in matches2:
    beginning = m.end() - 1
    temp_pattern = re.compile(r';')
    temp_matches = temp_pattern.finditer(test_code[beginning:])
    temp_all_find = []
    for m_temp in temp_matches:
        temp_all_find.append(m_temp.start())
    end = temp_all_find[0] + 1 + beginning
    all_index_to_remove.append(beginning)
    all_index_to_remove.append(end)   
    
pattern3 = re.compile(r'/\*')
matches3 = pattern3.finditer(test_code)

for m in matches3:
    beginning = m.end() - 2
    temp_pattern = re.compile(r'\*/')
    temp_matches = temp_pattern.finditer(test_code[beginning:])
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
    test_code = test_code[0:first_index] + test_code[end_index:]
    nb_of_removed_element += end_index - first_index



##################################

# Fin

##################################    
    
    
pattern4 = re.compile(r'SET [a-zA-Z0-9.&_ ]+[(;]')
matches4 = pattern4.finditer(test_code)

table_list = []
#set_matches = {matches,matches2}

for m in matches4:
    beginning = m.start()
    beginning += 3  #Afin de ne pas afficher le SET à chaque fois
    end = m.end()
    #print(beginning)
    table_list.append(test_code[beginning:end])
    
    
    
pattern5 = re.compile(r'FROM [a-zA-Z0-9._&]+[ (;\n]')
matches5 = pattern5.finditer(test_code)


for m in matches5:
    beginning = m.start()
    beginning += 4  #Afin de ne pas afficher le FROM à chaque fois
    end = m.end()
    #print(beginning)
    table_list.append(test_code[beginning:end])



###########################################
    
#      Traitement a part des "DATA="      #
    
###########################################   
    

pattern6 = re.compile(r'DATA ?= ?[a-zA-Z0-9._&]+[ ;(]')
matches6 = pattern6.finditer(test_code)
table_list_data = []

for m in matches6:
    beginning = m.start()
    beginning += 4  #Afin de ne pas afficher le DATA à chaque fois
    end = m.end()
    #print(beginning)
    table_list_data.append(test_code[beginning:end])


###########################################
    
#     Tables creees par le programme      #
    
###########################################   

prgm_table = []
pattern7 = re.compile(r'DATA [a-zA-Z0-9._&]+[ ;]')


matches7 = pattern7.finditer(test_code)


for m in matches7:
    beginning = m.start()
    beginning += 4  #Afin de ne pas afficher le DATA à chaque fois
    end = m.end()
    #print(beginning)
    prgm_table.append(test_code[beginning:end])
    
    
pattern8 = re.compile(r'CREATE TABLE [a-zA-Z0-9._&]+[ ;]')
matches8 = pattern8.finditer(test_code)

for m in matches8:
    beginning = m.start()
    beginning += 12  #Afin de ne pas afficher le CREATE TABLE à chaque fois
    end = m.end()
    #print(beginning)
    prgm_table.append(test_code[beginning:end])   
###########################################
    
#         Nettoyage des listes            #
    
###########################################   
    
    
def clean_list(list_to_clean):
    list_to_return = []
    for i in list_to_clean:
        #nettoyage du debut de la chain 
        temp_pattern = re.compile(r'[a-zA-Z0-9._&]+[ ;]')
        temp_matches = temp_pattern.finditer(i)
        #obligé de faire une boucle car certains SET contiennent plusieurs tables
        for m in temp_matches:
            beginning = m.start()
            end = m.end()
            end = end - 1 #Pour ne garder que les lettres composant le nom de la table
            list_to_return.append(i[beginning:end])
    return set(list_to_return)
    
set_table = clean_list(table_list)  
set_table_data = clean_list(table_list_data)
set_table_created = clean_list(prgm_table)

final_list = set_table - set_table_created
final_list_data = set_table_data - set_table_created


#Si on veut sortir un tableur pour les procedures SET/FROM et un pour celles DATA

#df1 = pd.DataFrame({'Tables requises pour faire tourner le code :':list(final_list)})
#df2 = pd.DataFrame({'Tables requises pour faire tourner le code (issues de procedure DATA = ) :':list(final_list_data)})
#df1.to_excel("C:/Users/Levesqgu/Desktop/tables_SAS.xlsx")
#df2.to_excel("C:/Users/Levesqgu/Desktop/tables_SAS_data.xlsx")

#Si on veut un seul et meme tableur sans doublon

final_list = set(final_list)|set(final_list_data)

df  = pd.DataFrame({'Tables requises pour faire tourner le code :':list(final_list)})
df.to_excel("...Desktop/tables_SAS.xlsx")   # Put your path here
