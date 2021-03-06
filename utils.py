from tkinter import *
import time
import random
from PIL import ImageTk, Image
import pandas as pd
from datetime import datetime
from operator import *
from tkinter import font

def annotate(df, col_name_file, col_class, path_folder_img, time_to_refresh, name_file):
    """
    List to create the new csv file
    """
    list_classes_user = []
    list_class_original = []
    list_file = []
    list_time = []

    list_appearance = []

    interface(list_classes_user, list_class_original, list_file, list_time, df, col_name_file, col_class, path_folder_img, time_to_refresh, list_appearance)

    i=0

    if len(list_classes_user) != len(list_class_original):
        list_classes_user.append("none")
        list_time.append("none")

    df_data = pd.DataFrame(list_classes_user, columns=['class by user'])
    df_data['original class'] = list_class_original
    df_data['file name'] = list_file
    df_data['check time'] = list_time

    df_app = pd.DataFrame(list_appearance, columns=['appearance'])
    df_app['file name'] = list_file

    df_data.to_csv(str(name_file)+".csv")
    df_app.to_csv(str(name_file) + "_appearance_" + ".csv")

def interface(list_classes_user, list_class_original, list_file, list_time, df, col_name_file, col_class, path_folder_img, time_to_refresh, list_appearance):
    # id of the visualize image thread
    jobs_id = []

    # create window
    window = Tk()
    # change color
    window['bg'] = '#BBDEF0'
    window.title("Pay attention")

    panel = Label(window)
    panel.grid(column=0, row=0, columnspan=3)

    lbl2 = Label(window, text="what do you see?", bg='#BBDEF0', font="System 19")
    lbl2.grid(column=0, row=2)

    # to save the value of "clicked"
    selected = StringVar()

    """
    The action of clicked the button about a label
    """
    def clicked():
        # update of the lists for the new data (annotation)
        # if you have already selected, the annotate doesn't save
        if len(list_class_original) - len(list_classes_user) == 1:
            # save the data
            list_classes_user.append(selected.get())
            list_time.append(datetime.now().time())
            # cancel the thread/open image
            cancel()
            # open new image
            jobs_id.append(window.after(0, change_image))

    def cancel():
        for job in jobs_id:
            window.after_cancel(job)

    get_radio_button(window, selected, clicked, labels=['computerroom', 'movietheater', 'library', 'kitchen', 'bowling', 'poolinside', 'trainstation', 'greenhouse'])

    """
    - To change the image
    - check how many image display
    """
    def change_image():
        print("start change image")
        print(datetime.now().time())

        """Check if the user annotated the last label, if not annotate none"""
        if len(list_class_original) != len(list_classes_user):
            print('none')
            list_classes_user.append('None')
            list_time.append(datetime.now().time())

        """Check if the experiment has end"""
        if len(list_class_original) == 2000:
            window.destroy()
        else:
            row = df.loc[random.randint(0, len(df)-1), :]
            """Annotate the img"""
            list_class_original.append(row[col_class])
            list_file.append(row[col_name_file])
            list_appearance.append(datetime.now().time())
            img = ImageTk.PhotoImage(Image.open(str((path_folder_img + row[col_name_file]))).resize((500, 500)))

            panel.configure(image=img)
            panel.image = img

            jobs_id.append(window.after(time_to_refresh, change_image))

    list_classes_user.append('START')
    list_file.append('START')
    list_class_original.append('START')
    list_time.append(datetime.now().time())
    #
    list_appearance.append(datetime.now().time())
    change_image()
    window.mainloop()

def get_radio_button(window, selected, clicked, labels):
    i = 0
    pos_col = 3
    temp = 0
    for label in labels:
        b = Radiobutton(window, text=label, variable=selected, bg='#BBDEF0', font="System 18 bold", value=label, command=clicked)

        if mod(i, 2) == 0:
            b.grid(column=0, row=pos_col, sticky=W)
            temp = pos_col
        else:
            b.grid(column=1, row=temp, sticky=W)
            pos_col = pos_col + 1
        i = i + 1
