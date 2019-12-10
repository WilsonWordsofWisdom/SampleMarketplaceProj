import pandas as pd
class Items:
    def __init__(self):
        self.df = pd.DataFrame([('book', '1'), ('ipad', 4)], columns=['name', 'price'])
    def add(self, item):
        self.df = self.df.append(pd.Series(item),ignore_index=True)
    def get_items(self, fitler=None):
        if fitler is None:
            return self.df# .loc[name]