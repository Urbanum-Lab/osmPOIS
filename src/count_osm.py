import pandas as pd

df = pd.read_csv("data/processed/osm_features.tsv", sep="\t")

areas = ["l5", "l6", "l7", "l8"]
for area in areas:
    df_key = df.groupby([area, "key"]).size()
    df_key.to_csv(f"data/aggregated/osm/key_{area}.tsv", sep="\t")
    df_value = df.groupby([area, "value"]).size()
    df_value.to_csv(f"data/aggregated/osm/value_{area}.tsv", sep="\t")
