import os
import pandas as pd
from sklearn.model_selection import train_test_split

data_folder = "txt_sentoken/"
folders = ["neg", "pos"]

data_folder = "bbc/"
folders = ["business","entertainment","politics","sport","tech"]

os.chdir(data_folder)

x = []
y = []

for i in folders:
    files = os.listdir(i)
    for text_file in files:
        file_path = i + "/" +text_file
        print("reading file:", file_path)
        with open(file_path) as f:
            data = f.readlines()
        data = ' '.join(data)
        x.append(data)
        y.append(i)
   
data = {'news': x, 'type': y}       
df = pd.DataFrame(data)

#To replace the string values with the unique integer value.
df['type_integer'] = pd.factorize(df.type)[0] + 1
print (df)

print('writing csv flie ...')
df.to_csv('../dataset_0_1.csv', index=False)