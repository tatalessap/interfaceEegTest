from tkinter import *
from tkinter.ttk import *
import time
import random
from PIL import ImageTk, Image
import pandas as pd


def annotate(df, col_name_file, col_class, path_folder_img, time_to_refresh, time_to_black):
    """
    List to create the new csv file
    """
    list_classes_user = []
    list_class_original = []
    list_file = []
    list_time = []

    interface(list_classes_user, list_class_original, list_file, list_time, df, col_name_file, col_class,
              path_folder_img, time_to_refresh, time_to_black)

    df_data = pd.DataFrame(list_classes_user, columns=['class by user'])
    df_data['original class'] = list_class_original
    df_data['file name'] = list_file
    df_data['check time'] = list_time

    df_data.to_csv("prova.csv")

def interface(list_classes_user, list_class_original, list_file, list_time, df, col_name_file, col_class,
              path_folder_img, time_to_refresh, time_to_black):
    list_it=[]

    print("start interface")
    # create window<
    window = Tk()
    window.title("Pay attention")

    """
    To check the time
    """
    tick = time.time()

    panel = Label(window)
    panel.grid(column=0, row=0, columnspan=3)

    lbl2 = Label(window, text="what do you see?")
    lbl2.grid(column=0, row=2)

    # to save the value of "clicked"
    selected = StringVar()

    def clicked():
        # update of the lists for the new data (annotation)
        # if you have already selected, the annotate doesn't save
        if len(list_class_original) - len(list_classes_user) == 1:
            print("Annotate")
            print(selected.get())
            list_classes_user.append(selected.get())
            list_time.append((time.time() - tick) / 60)

    button_face(window, selected, clicked)

    def call_back():
        img2 = ImageTk.PhotoImage(Image.open('black.jpg').resize((500, 500)))
        panel.configure(image=img2)
        panel.image = img2

    # to change image
    def change_image():
        print("start change image")

        """Check if the user annotated the last label, if not annotate none"""
        if len(list_class_original) != len(list_classes_user):
            print('none')
            list_classes_user.append('None')
            list_time.append((time.time() - tick) / 60)

        """Check if the experiment has end"""
        if len(list_class_original) == 10:
            window.destroy()
        else:
            if len(list_it) == 0:
                img = ImageTk.PhotoImage(Image.open('black.jpg').resize((500, 500)))
                list_it.append(1)

            else:
                row = df.loc[random.randint(0, len(df)), :]
                """Annotate the img"""
                list_class_original.append(row[col_class])
                list_file.append(row[col_name_file])
                print("open image")
                img = ImageTk.PhotoImage(Image.open(str((path_folder_img + row[col_name_file]))).resize((500, 500)))

            panel.configure(image=img)
            panel.image = img

            print("Start black image")
            window.after(time_to_black, call_back)

            print("change image")
            window.after(time_to_refresh, change_image)

    change_image()

    window.mainloop()

def button_animals(window, selected, clicked):
        scoiattolo_radioB = Radiobutton(window, text='scoiattolo', value='scoiattolo', variable=selected, command=clicked)

        cane_radioB = Radiobutton(window, text='cane', value='cane', variable=selected, command=clicked)

        pecora_radioB = Radiobutton(window, text='pecora', value='pecora', variable=selected, command=clicked)

        ragno_radioB = Radiobutton(window, text='ragno', value='ragno', variable=selected, command=clicked)

        gatto_radioB = Radiobutton(window, text='gatto', value='gatto', variable=selected, command=clicked)

        cavallo_radioB = Radiobutton(window, text='cavallo', value='cavallo', variable=selected, command=clicked)

        elefante_radioB = Radiobutton(window, text='elefante', value='elefante', variable=selected, command=clicked)

        farfalla_radioB = Radiobutton(window, text='farfalla', value='farfalla', variable=selected, command=clicked)

        mucca_radioB = Radiobutton(window, text='mucca', value='mucca', variable=selected, command=clicked)

        gallina_radioB = Radiobutton(window, text='gallina', value='gallina', variable=selected, command=clicked)

        scoiattolo_radioB.grid(column=0, row=3, sticky=W)

        cane_radioB.grid(column=1, row=3, sticky=W)

        pecora_radioB.grid(column=0, row=4, sticky=W)

        ragno_radioB.grid(column=1, row=4, sticky=W)

        gatto_radioB.grid(column=0, row=5, sticky=W)

        cavallo_radioB.grid(column=1, row=5, sticky=W)

        elefante_radioB.grid(column=0, row=6, sticky=W)

        farfalla_radioB.grid(column=1, row=6, sticky=W)

        mucca_radioB.grid(column=0, row=7, sticky=W)

        gallina_radioB.grid(column=1, row=7, sticky=W)


def button_face(window, selected, clicked):
    button_1 = Radiobutton(window, text='angry', value='angry', variable=selected, command=clicked)

    button_2 = Radiobutton(window, text='disgust', value='disgust', variable=selected, command=clicked)

    button_3 = Radiobutton(window, text='fear', value='fear', variable=selected, command=clicked)

    button_4 = Radiobutton(window, text='neutral', value='neutral', variable=selected, command=clicked)

    button_5 = Radiobutton(window, text='sadness', value='sadness', variable=selected, command=clicked)

    button_6 = Radiobutton(window, text='surprise', value='surprise', variable=selected, command=clicked)

    button_7 = Radiobutton(window, text='happiness', value='happiness', variable=selected, command=clicked)

    #

    button_1.grid(column=0, row=3, sticky=W)

    button_2.grid(column=1, row=3, sticky=W)

    button_3.grid(column=0, row=4, sticky=W)

    button_4.grid(column=1, row=4, sticky=W)

    button_5.grid(column=0, row=5, sticky=W)

    button_6.grid(column=1, row=5, sticky=W)

    button_7.grid(column=1, row=6, sticky=W)


