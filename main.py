from utils import *
import pandas as pd


eti = ['scoiattolo', 'cane', 'pecora', 'ragno', 'gatto', 'cavallo', 'elefante', 'farfalla', 'mucca', 'gallina']

df = pd.read_csv('dataset_animals.csv', index_col=0)

list_classes_user = []
list_class_original = []
list_file = []
list_time = []

tick = time.time()

"""
for i in range(1, 10):
    interface(list_classes_ut, list_class_original, list_file, list_time, df, 6000, tick)
"""

interface(list_classes_user, list_class_original, list_file, list_time, df, 3000, 2000, tick)

if len(list_class_original) != len(list_classes_user):
    print('none')
    list_classes_user.append('None')
    list_time.append((time.time() - tick) / 60)

df_data = pd.DataFrame(list_classes_user, columns=['class by user'])
df_data['original class'] = list_class_original
df_data['file name'] = list_file
df_data['check time'] = list_time

df_data.to_csv("prova.csv")

i=0
