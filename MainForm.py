from tkinter import *

from matplotlib.backends.backend_tkagg \
    import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from files import *


class MainForm:
    xls_file_name = 'Graph.xls'
    form = Tk(className='Строим график')

    def __init__(self):
        self.form.wm_minsize(width=700, height=600)
        self.openGraphButton = Button(self.form, text='Построить график', command=self.create_graf)
        self.openGraphButton.pack(side='top')

        self.form.mainloop()

    def create_graf(self):
        data = read_xls_file(self.xls_file_name)

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
