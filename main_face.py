from utils import *
import pandas as pd

"""
CSV with labels, name file
"""
df = pd.read_csv('/home/tatalessap/db_faces/data.csv')

"""
Method to display the interface and annotate the images
"""
col_name_file = 'filepath'
col_class = 'facial_expression'
path_folder_img = '/home/tatalessap/db_faces/'

#time_to_refresh, time_to_black
annotate(df, col_name_file, col_class, path_folder_img, 3000, 5000)

i=0
