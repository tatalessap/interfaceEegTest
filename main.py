from utils import *
import pandas as pd

"""
CSV with labels, name file
"""
df = pd.read_csv('image.csv', index_col=0)

"""
Method to display the interface and annotate the images
"""
col_name_file = 'name_file'
col_class = 'class'
path_folder_img = 'ALL/'

# time_to_refresh, time_to_black
annotate(df, col_name_file, col_class, path_folder_img, 7000)

i=0
