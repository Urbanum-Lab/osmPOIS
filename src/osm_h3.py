import h3
import pandas as pd
import pyrosm
from pyrosm import get_data

osm_file = "data/raw/Budapest.osm.pbf"
fp = get_data(
    "Budapest",
    directory="data/raw",
)
osm = pyrosm.OSM(fp)

pois = osm.get_pois()

useful = [
    "amenity",
    "building",
    "craft",
    "emergency",
    "highway",
    "cycleway",
    "landuse",
    "leisure",
    "office",
    "power",
    "public_transport",
    "railway",
]

with open("data/processed/osm_features.tsv", "w") as outfile:
    h = "key\tvalue\tlat\tlon\tl5\tl6\tl7\tl8\n"
    outfile.write(h)
    for _, row in pois.iterrows():
        lat = row["lat"]
        lon = row["lon"]
        t = row["osm_type"]
        if not (pd.isnull(lat) and pd.isnull(lon)):
            poi_data = row.dropna()
            for key in useful:
                try:
                    value = poi_data[key]
                    l5 = h3.geo_to_h3(lat, lon, 5)
                    l6 = h3.geo_to_h3(lat, lon, 6)
                    l7 = h3.geo_to_h3(lat, lon, 7)
                    l8 = h3.geo_to_h3(lat, lon, 8)
                    o = "\t".join([key, value, str(lat), str(lon), l5, l6, l7, l8])
                    outfile.write(o + "\n")
                except Exception as e:
                    continue
