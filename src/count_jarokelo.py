import pandas as pd

df = pd.read_csv("data/processed/jarokelo_hashed.tsv", sep="\t")
df.drop(columns=["lat", "lon"], inplace=True)
levels = ["l5", "l6", "l7", "l8"]
for level in levels:
    df_level = df.groupby([level, "Category"]).size()
    df_level.to_csv(f"data/aggregated/jarokelo/jarokelo_{level}.tsv", sep="\t")
