import pandas as pd
import os

df = {
    "Name" : ["Keerthi", "Keerthi N", "Keerthi N Kumar"],
    "Age" : [21, 22, 18],
    "City" : ["Bangalore", "Mysore", "Tumkur"]
}

df = pd.DataFrame(df)

data_dir = 'data'

new_row = {'Name' : "Ram", "Age" : 21, "City" : "Ayodhya"}
df.loc[len(df.index)] = new_row

new_row1 = {'Name' : "Sita", "Age" : 20, "City" : "Janaka"}
df.loc[len(df.index)] = new_row1

os.makedirs(data_dir, exist_ok=True)

# define path

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")