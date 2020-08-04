from tkinter import *
from tkinter.ttk import *
import time
import random
from PIL import ImageTk, Image


def interface(list_classes_ut, list_class_original, list_file, list_time, df, time_to_refresh, tick):
    window = Tk()
    window.title("Pay attention")

    row = df.loc[random.randint(0, len(df)), :]
    f = row['name_file']
    cl = row['class']

    # open the image
    path_img = str(('all_image/' + f))
    img = Image.open(path_img)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)

    panel = Label(window, image=img)
    panel.grid(column=0, row=0, columnspan=3)

    lbl2 = Label(window, text="what animal do you see?")
    lbl2.grid(column=0, row=2)

    selected = StringVar()

    def clicked():
        print(selected.get())
        list_classes_ut.append(selected.get())
        list_class_original.append(cl)
        list_file.append(f)
        list_time.append((time.time() - tick) / 60)

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

    # pos

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

    window.after(time_to_refresh, window.destroy)

    window.mainloop()
