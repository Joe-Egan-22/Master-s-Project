import pandas as pd

def read_data(settings):

    vars = pd.read_csv(settings['file'])

    return vars