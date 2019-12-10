import pandas as pd

class Users:
    def __init__(self):
        self.df = pd.read_csv('Users.csv')

    def register(self, input_dict):
        self.df = self.df.append(pd.Series(input_dict),ignore_index=True)
        self.df.to_csv('Users.csv', index=False)
