import pandas as pd

class Offer:

    def __init__(self):
        self.df = pd.read_csv('Offers.csv')

    def add(self, offer, save=False):
        self.df = self.df.append(pd.Series(offer),ignore_index=True)
        if save:
            self.df.to_csv('Offers.csv', index=False)
            

        