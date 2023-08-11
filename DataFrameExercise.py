import pandas as pd
import numpy as np


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#123
#given the data above, create a datafram using the labels as row indexes and perform the following tasks#







""" 
(1)  Select the 'name' and 'score' columns from the DataFrame.

Expected Output:
        name  score                                                    
a  Anastasia   12.5                                                    
b       Dima    9.0                                                    
c  Katherine   16.5                                                    
d      James    NaN                                                    
e      Emily    9.0                                                    
f    Michael   20.0                                                    
g    Matthew   14.5                                                    
h      Laura    NaN                                                    
i      Kevin    8.0                                                    
j      Jonas   19.0 
"""






"""
(2) Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the data frame.

Expected Output:
   score qualify
b    9.0      no
d    NaN      no
f   20.0     yes
g   14.5     yes

"""






"""
(3)  Select the rows where the number of attempts in the examination is greater than 2

Expected Output:
      name  score  attempts qualify
b     Dima    9.0         3      no
d    James    NaN         3      no
f  Michael   20.0         3     yes                    

"""






"""
(4) Select the rows the score is between 15 and 20 (inclusive).

Expected Output:
   attempts    name         qualify     score                                  
c         2    Katherine     yes        16.5                                  
f         3    Michael       yes        20.0                                  
j         1      Jonas       yes        19.0   

"""






"""
(5) sort a given DataFrame by two or more columns - attempts, name

Expected Output:
   attempts       name qualify  score
0         1  Anastasia     yes   12.5
9         1      Jonas     yes   19.0
7         1      Laura      no    NaN
6         1    Matthew     yes   14.5
4         2      Emily      no    9.0
2         2  Katherine     yes   16.5
8         2      Kevin      no    8.0
1         3       Dima      no    9.0
3         3      James      no    NaN
5         3    Michael     yes   20.0 

"""




