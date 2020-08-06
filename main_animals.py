from utils import *
import pandas as pd

"""
Labels
"""
eti = ['scoiattolo', 'cane', 'pecora', 'ragno', 'gatto', 'cavallo', 'elefante', 'farfalla', 'mucca', 'gallina']

"""
CSV with labels, name file
"""
df = pd.read_csv('dataset_animals.csv', index_col=0)

"""
Method to display the interface and annotate the images
"""
col_name_file = 'name_file'
col_class = 'class'
path_folder_img = 'all_image/'

#time_to_refresh, time_to_black
annotate(df, col_name_file, col_class, path_folder_img, 3000, 4000)

i=0
