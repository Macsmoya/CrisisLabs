import pandas as pd
def get_dataframe(channel):
    df = pd.read_csv('data/' + channel + '.csv') #Read data from data.csv
    df.columns=['x','y']
    return df

quakelst = [0]
df = get_dataframe('EHZ')
for index, row in df.iterrows():
        if int(abs(row['y'])) > 30000:
            quakelst.append(int(abs(row['y'])))
        elif quakelst[-1] != False:
            quakelst.append(False)
        print(quakelst)    
