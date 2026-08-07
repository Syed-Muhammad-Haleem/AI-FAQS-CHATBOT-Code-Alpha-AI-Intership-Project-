import pandas as pd
class DataSetLoader:
    def __init__(self):
        self.dataset=None

    def load_dataset(self):
        self.dataset=pd.read_csv("dataset/faq.csv",sep='|')
        return self.dataset

