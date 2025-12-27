import pandas as pd
import sys
import os

df = pd.DataFrame({"a":[1,2,3], "b":[5,6,7]})
print(df.head())

data = sys.argv[1]

os.makedirs("output", exist_ok=True)

df.to_csv(f"output/output_{data}.csv", index =False)

print(f"hi pipeline, month = {data}")
