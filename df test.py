import pandas as pd
def get_dataframe(channel):
    df = pd.read_csv('data/' + channel + '.csv') #Read data from data.csv
    df.columns=['x','y']
    return df
 
print(str(get_dataframe('EHZ')))
