import matplotlib.pyplot as plt

def plot_point(point):
    global plt
    plt.plot([point.x], [point.y], 'ro')
def plot_line(line):
    pass


class Plot:

    def __init__(self, lst_of_element_to_plot):
        self.elements = lst_of_element_to_plot
        for item in self.elements:
            type = item.__class__.__name__

            if type == "Point":
                plot_point(item)


            if type == "Line":
                plot_line(item)
        plt.show()