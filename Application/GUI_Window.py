import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk


class Figure1(object):


    def __init__(self, root = tk.Tk()):

        self.root = root
        self.start_parameters()
        print('Creating figure 1...')


    def root_mainloop_start(self):
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def start_parameters(self):
        self.root.geometry('1200x800')
        # self.root.resizable(False, False)
        self.root.title('Figure1')

    def column_graph(self, main, postprocessing):
        self.fig = Figure(figsize=(12, 7.6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.chart = FigureCanvasTkAgg(self.fig, master=self.root)
        self.ax.grid()
        self.ax.set_aspect('equal', adjustable='box')


        self.add_plot_to_column_graph(main.smaller_range_limits_enu, 'red', 'EPD53 A')
        self.add_plot_to_column_graph(main.range_limits_enu, 'blue', 'EPD53 B')
        self.add_plot_to_column_graph(main.range_sea_limits_enu, '#ff9900', 'P-24 i P-20')
        self.add_plot_to_column_graph(main.range_shore_enu, '#ffcc80', 'Brzeg')
        self.ax.plot((main.launchpad_launch_vector[0], main.launchpad_launch_vector[2]),
                     (main.launchpad_launch_vector[1], main.launchpad_launch_vector[3]), color='grey', linewidth=0.5)



        self.add_scatter_to_column_graph(postprocessing.create_impact_points()[0], 'red', 'Rakieta')
        self.add_scatter_to_column_graph(postprocessing.create_impact_points()[1], 'green', 'Booster')
        self.add_scatter_to_column_graph(postprocessing.create_impact_points()[2], 'blue', 'Payload')

        circle1 = plt.Circle((0, 0), 1.0, color='black', fill=False, label='Miejsce Startu')
        self.ax.add_patch(circle1)


        self.ax.add_patch(Ellipse(
            (postprocessing.mean()[0][0]/1e3, postprocessing.mean()[0][1]/1e3),
            postprocessing.sim_calculations()[0]['sim_crossrange_stdev']*6/1e3,
            postprocessing.sim_calculations()[0]['sim_downrange_stdev']*6/1e3,
            (360-postprocessing.downgrade_line_theta()[0]),
            fill=False, label='Rocket 3 sigma', color='#FF0000', linewidth=2))

        self.ax.add_patch(Ellipse(
            (postprocessing.mean()[1][0] / 1e3, postprocessing.mean()[1][1] / 1e3),
            postprocessing.sim_calculations()[1]['sim_crossrange_stdev']*6 / 1e3,
            postprocessing.sim_calculations()[1]['sim_downrange_stdev']*6 / 1e3,
            (360 - postprocessing.downgrade_line_theta()[1]),
            fill=False, label='Booster 3 sigma', color='#00FF00', linewidth=2))

        self.ax.add_patch(Ellipse(
            (postprocessing.mean()[2][0] / 1e3, postprocessing.mean()[2][1] / 1e3),
            postprocessing.sim_calculations()[2]['sim_crossrange_stdev']*6 / 1e3,
            postprocessing.sim_calculations()[2]['sim_downrange_stdev']*6 / 1e3,
            (360 - postprocessing.downgrade_line_theta()[2]),
            fill=False, label='Booster 3 sigma', color='#0000FF', linewidth=2))


        self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))


        toolbar = NavigationToolbar2Tk(self.chart, self.root)
        self.chart.draw()
        self.chart.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)
        self.ax.set_xlabel('Odleglosc S-N [km]')
        self.ax.set_ylabel('Odleglosc W-E [km]')

        toolbar.update()


        # self.root_mainloop_start()

    def add_scatter_to_column_graph(self, data, color_kind, label):
        x = []
        y = []
        for k in data:
            x.append(k[0] / 1e3)
            y.append(k[1] / 1e3)
        self.ax.scatter(x, y, label=label, facecolors='none', edgecolors=color_kind, s=20, linewidths=0.5)

    def add_plot_to_column_graph(self, data, color_kind, label_kind):
        x = []
        y = []
        for k in data:
            x.append(k[0]/1e3)
            y.append(k[1]/1e3)
        self.ax.plot(x, y, color=color_kind, linewidth=0.5, label=label_kind)

class Figure2(object):


    def __init__(self, root=tk.Tk()):
        self.root = root
        self.start_parameters()
        print('Creating figure 2...')


    def root_mainloop_start(self):
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def start_parameters(self):
        self.root.geometry('1200x800')
        # self.root.resizable(False, False)
        self.root.title('Figure2')

    def column_graph(self, postprocessing):
        self.fig = Figure(figsize=(12, 7.6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.chart = FigureCanvasTkAgg(self.fig, master=self.root)
        self.ax.grid()
        self.ax.set_aspect('equal', adjustable='box')



        self.add_scatter_to_column_graph(postprocessing.range()[2], 'blue')


        self.ax.add_patch(Ellipse(
            (postprocessing.sim_calculations()[2]['sim_crossrange_mean'] / 1e3, postprocessing.sim_calculations()[2][
                'sim_downrange_mean'] / 1e3),
            postprocessing.sim_calculations()[2]['sim_crossrange_stdev']*2/1e3,
            postprocessing.sim_calculations()[2]['sim_downrange_stdev']*2/1e3,
            0,
            fill=False, color='#4d4dff', linewidth=2))

        self.ax.add_patch(Ellipse(
            (postprocessing.sim_calculations()[2]['sim_crossrange_mean']/1e3, postprocessing.sim_calculations()[2][
                'sim_downrange_mean']/1e3),
            postprocessing.sim_calculations()[2]['sim_crossrange_stdev']*4 / 1e3,
            postprocessing.sim_calculations()[2]['sim_downrange_stdev']*4 / 1e3,
            0,
            fill=False, color='#cc0000', linewidth=2))

        self.ax.add_patch(Ellipse(
            (postprocessing.sim_calculations()[2]['sim_crossrange_mean'] / 1e3, postprocessing.sim_calculations()[2][
                'sim_downrange_mean'] / 1e3),
            postprocessing.sim_calculations()[2]['sim_crossrange_stdev']*6 / 1e3,
            postprocessing.sim_calculations()[2]['sim_downrange_stdev']*6 / 1e3,
            0,
            fill=False, color='#ffa31a', linewidth=2))



        toolbar = NavigationToolbar2Tk(self.chart, self.root)
        self.chart.draw()
        self.chart.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)

        toolbar.update()


        self.root_mainloop_start()


    def add_scatter_to_column_graph(self, data, color_kind):
        x = []
        y = []
        for k in data:
            x.append(k[0] / 1e3)
            y.append(k[1] / 1e3)
        self.ax.scatter(x, y, facecolors='none', edgecolors=color_kind, s=20, linewidths=0.5)


