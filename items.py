import pandas as pd
from icecream import ic
from loguru import logger

ic.configureOutput(outputFunction=lambda s: logger.debug(s))
ic.configureOutput(includeContext=True)
ic.configureOutput(prefix="")

class Items:

    def __init__(self):
        self.df = pd.read_csv('Products.csv')
        ic(self.df)

    def add(self, item, save=False):
        self.df = self.df.append(pd.Series(item),ignore_index=True)
        if save:
            self.df.to_csv('Products.csv', index=False)
        return self.df

    def get_items(self, filter_names=None):
        if filter_names is None:
            return self.df
        else:
            return self.df.loc[filter_names]
        