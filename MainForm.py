from tkinter import *

from matplotlib.backends.backend_tkagg \
    import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from files import *


class MainForm:
    form = Tk(className='Строим график')

    def __init__(self):
        self.form.wm_minsize(width=700, height=600)
        self.openGraphButton = Button(self.form, text='Построить график', command=self.open_file)
        self.openGraphButton.pack(side='top')

        self.form.mainloop()

    def open_file(self):
        xls_file_name = open_window()
        self.create_graf(xls_file_name)

    def create_graf(self, xls_file_name):
        data = read_xls_file(xls_file_name)

        x = data.values[:, 0]
        y = data.values[:, 1]

        f = Figure()
        plot = f.add_subplot(111)

        plot.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self.form)

        toolbar = NavigationToolbar2Tk(canvas, self.form)
        toolbar.update()

        canvas.tkcanvas.pack()


MainForm()
