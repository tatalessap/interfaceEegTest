from tkinter import *
from tkinter.ttk import *
import time
import random
from PIL import ImageTk, Image


def interface(list_classes_user, list_class_original, list_file, list_time, df, time_to_refresh, time_to_black, tick):
    # create window
    window = Tk()
    window.title("Pay attention")

    # insert first image

    # open the image
    img = Image.open("black.jpg")
    img2 = ImageTk.PhotoImage(Image.open('black.jpg').resize((300, 300)))
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)

    # organizer the interface (grid etc)
    panel = Label(window, image=img)
    panel.grid(column=0, row=0, columnspan=3)

    lbl2 = Label(window, text="what animal do you see?")
    lbl2.grid(column=0, row=2)


    # to save the value of "clicked"
    selected = StringVar()

    def clicked():
        # update of the lists for the new data (annotation)
        print(selected.get())
        list_classes_user.append(selected.get())
        list_time.append((time.time() - tick) / 60)

    # buttons
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

    # end buttons

    def call_back():
        img2 = ImageTk.PhotoImage(Image.open('black.jpg').resize((250, 250)))
        panel.configure(image=img2)
        panel.image = img2

    # to change image
    def change_image():
        print(len(list_classes_user))
        print(len(list_class_original))
        if len(list_class_original) != len(list_classes_user):
            print('none')
            list_classes_user.append('None')
            list_time.append((time.time() - tick) / 60)

        row = df.loc[random.randint(0, len(df)), :]
        f = row['name_file']
        cl = row['class']

        # open the image
        path_img = str(('all_image/' + f))
        img = Image.open(path_img)
        img = ImageTk.PhotoImage(img.resize((250, 250)))
        panel.configure(image=img)
        panel.image = img
        list_class_original.append(cl)
        list_file.append(f)

        window.after(time_to_black, call_back)

        print("change image")

        window.after(time_to_refresh, change_image)

    change_image()

    window.mainloop()

