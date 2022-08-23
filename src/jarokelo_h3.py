import h3
import pandas as pd

df = pd.read_csv("data/raw/2022 Urbanum - összes ügy tsv", sep="\t")

with open("data/processed/jarokelo_hashed.tsv", "w") as outfile:
    h = "Category\tlat\tlon\tl5\tl6\tl7\tl8\n"
    outfile.write(h)
    for _, row in df.iterrows():
        lat = row["Lat"]
        lon = row["Lng"]
        category = row["Kategoria"]
        l5 = h3.geo_to_h3(lat, lon, 5)
        l6 = h3.geo_to_h3(lat, lon, 6)
        l7 = h3.geo_to_h3(lat, lon, 7)
        l8 = h3.geo_to_h3(lat, lon, 8)
        o = "\t".join([category, str(lat), str(lon), l5, l6, l7, l8])
        outfile.write(o + "\n")
