import pandas as pd
import os


current_dir = os.getcwd()


load_file = pd.read_csv(f"{current_dir}/pandas/data.csv", index_col='Name')


print(load_file.iloc['Name'])
