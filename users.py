import pandas as pd

class Users:
    def __init__(self):
        self.df = pd.read_csv('Users.csv')

    def register(self, input_dict, save=False):
        self.df = self.df.append(pd.Series(input_dict),ignore_index=True)
        if save:
            self.df.to_csv('Users.csv', index=False)
