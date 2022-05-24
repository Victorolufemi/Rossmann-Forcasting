import matplotlib.pyplot as plt
import pandas as pd
class eda():

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def data_shape(self, data: pd.DataFrame):
        print(data.name, 'shape:', data.shape)


    # function to ckeck the size of a dataset
    def data_size(self, data: pd.DataFrame):
        print(data.name, 'size:', data.size)


    # function to ckeck the information of a dataset
    def data_info(self, data: pd.DataFrame):
        print(data.name, 'information:')
        print('********')
        print(data.info())
        print('********')


    # function to get all unique values in the categorical variables
    def unique_val(self, data: pd.DataFrame):
        cols = data.columns
        for i in cols:
            if data[i].dtype == 'O':
                print('Unique values in', i, 'are', data[i].unique())
                print('----------------------------------------------')


    # function to ckeck for missing values
    def missing_val(self, data: pd.DataFrame):
        print('Sum of missing values in', data.name)
        print('------------------------------')
        print(data.isnull().sum())
        print('------------------------------')


    """
    VISUALIZATION
    """


    def fig_att2(self,title, title_x, title_y, size, size_xy, weight):
        plt.title(title, size=size, weight=weight)
        plt.xlabel(title_x, size=size_xy, weight=weight)
        plt.ylabel(title_y, size=size_xy, weight=weight)


    def fig_size(self, x, y):
        plt.figure(figsize=(x, y))


    def get_value(self, figure):
        for p in figure.patches:
            figure.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2.,
                                                     p.get_height()), ha='center', va='center',
                            xytext=(0, 10), textcoords='offset points')


    def fig_att(self, figure, title, title_x, title_y, size, size_xy, weight):
        figure.set_title(title, size=size, weight=weight)
        figure.set_xlabel(title_x, size=size_xy, weight=weight)
        figure.set_ylabel(title_y, size=size_xy, weight=weight)


    def rotate(self, figure, rotation):
        for item in figure.get_xticklabels():
            item.set_rotation(rotation)


    def save(self, name):
        plt.savefig(f"{name}.png")