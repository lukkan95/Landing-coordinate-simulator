from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from main import *

class Window(object):


    def __init__(self, root=tk.Tk()):
        self.root = root
        self.start_parameters()
        self.column_graph()


    def root_mainloop(self):
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def start_parameters(self):
        self.root.geometry('1200x800')
        self.root.resizable(False, False)
        self.root.title('Figure1')

    def column_graph(self):
        self.fig = Figure(figsize=(12, 7.6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        # df = {'x_pos': [1, 1], 'y_pos': [2, 3], 'color': 'red'}
        # self.ax.plot(smaller_range_limits_enu)
        # self.ax.scatter('x_pos', 'y_pos', data=df1, c='color')
        self.add_plot_to_column_graph(smaller_range_limits_enu, 'red')
        self.add_plot_to_column_graph(range_limits_enu, 'blue')
        self.add_plot_to_column_graph(range_sea_limits_enu, 'green')
        self.add_plot_to_column_graph(range_shore_enu, 'brown')
        self.chart = FigureCanvasTkAgg(self.fig, master=self.root)
        self.chart.draw()
        self.chart.get_tk_widget().pack(side=tk.TOP, expand=1)
        self.ax.set_xlabel('Odleglosc S-N [km]')
        self.ax.set_ylabel('Odleglosc W-E [km]')
        toolbar = NavigationToolbar2Tk(self.chart, self.root)
        toolbar.update()

    def add_scatter_to_column_graph(self, data):
        df1 = {'x_pos': [5, 5], 'y_pos': [7, data], 'color': 'green'}
        self.ax.scatter('x_pos', 'y_pos', data=df1, c='color')

    def add_plot_to_column_graph(self, data, color_kind):
        x = []
        y = []
        for k in data:
            x.append(k[0]/1e3)
            y.append(k[1]/1e3)
        self.ax.plot(x, y, color=color_kind, linewidth=0.5)


zap1 = Window()
zap1.root_mainloop()
