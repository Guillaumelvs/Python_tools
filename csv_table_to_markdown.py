"""
Created on Thu Oct 14 17:46:25 2021

@author: Guillaumelvs

Obtenir un tableau markdown à partir d'un csv :
    
    Alignement :
    
        --- Le contenu est aligné à gauche
        :-: le contenu est centré
        --: le contenu est aligné à droite

"""
import pandas as pd
import numpy as np
my_path = ' .csv'  # put your csv file path here
df = pd.read_csv(my_path, sep=";", encoding = "ISO-8859-1")
shape_df = df.shape
list_col = df.columns.tolist()
final_output = ""


for i in list_col :
    final_output = final_output + ' | ' + i
    df[i] = ' | ' + df[i].astype(str)
    
    
df[list_col[-1]] = df[i] + ' | \n'
final_output = final_output + ' | \n'



for i in range(shape_df[1]) : 
    final_output = final_output + ' | :-:'
    
    
    
final_output = final_output + ' | \n'
numpy_df = np.array(df)


for i in range(shape_df[0]) : 
    for j in range(shape_df[1]) : 
        final_output = final_output + numpy_df[i,j]
        
        
print(final_output)