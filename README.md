# Getting OSM POIS & Geohashing Jarokelo datapoints

A simple project that
- gets osm pbf for a given city (or other territory)
- and collects each and every OSM map features with
their lat-lon
- using H3 is geohashes each entry
- and saves the results into a nice tsv
- add H3 geohashes to each Jarokelo datapoint

**Warning:** The code is not optimal, this is just a 
quick and dirty solution for a problem we encountered.