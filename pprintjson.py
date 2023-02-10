import json
import pandas as pd

file_path = "./data/qgis_epsg4326.geojson"
#json = pd.read_json(file_path)
#parsed = json.dumps(json.loads(json), indent=4)
with open(file_path) as f:
    gj = json.load(f)
parsed = json.dumps(gj, indent=4)
outdir = "./data/qgis_epsg4326.json"
with open(outdir, "w") as outfile:
    outfile.write(parsed)


