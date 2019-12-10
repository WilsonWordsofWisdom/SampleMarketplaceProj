import pandas as pd

class Items:

    def __init__(self):
        self.df = pd.read_csv('Products.csv')

    def add(self, item):
        self.df = self.df.append(pd.Series(item),ignore_index=True)

    def get_items(self, filter_names=None):
        if filter_names is None:
            return self.df
        else:
            return df.loc[filter_names]
        