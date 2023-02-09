import geojson
import geopandas as gpd

file_path = "./data/segments.geojson"
with open(file_path) as f:
    gj = geojson.load(f)

crs = gj.crs['properties']['name']
collection = geojson.FeatureCollection(gj['features'])
gdf = gpd.GeoDataFrame.from_features(
    collection['features'],
    crs=crs.split(':')[1]
)

gdf = gdf.to_crs(4326)
gdf.to_file("./data/segments_epsg4326.json", driver="GeoJSON")
