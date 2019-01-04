import pandas as pd

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./mpg.csv")
df = pd.read_csv(file_path)
print(df)
