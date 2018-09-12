import pandas as pd

inpath = "../inputs/sales.csv"
outpath = "../outputs/pd_df.csv"

# Load csv
df = pd.read_csv(inpath)

print(df)

df.to_csv(outpath)
