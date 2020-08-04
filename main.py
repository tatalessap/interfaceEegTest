from utils import *
import pandas as pd


eti = ['scoiattolo', 'cane', 'pecora', 'ragno', 'gatto', 'cavallo', 'elefante', 'farfalla', 'mucca', 'gallina']

df = pd.read_csv('dataset_animals.csv', index_col=0)

list_classes_ut = []
list_class_original = []
list_file = []
list_time = []

tick = time.time()


for i in range(1, 10):
    interface(list_classes_ut, list_class_original, list_file, list_time, df, 5000, tick)

df_data = pd.DataFrame(list_classes_ut, columns=['class by user'])
df_data['original class'] = list_class_original
df_data['file name'] = list_file
df_data['check time'] = list_time

i=0
