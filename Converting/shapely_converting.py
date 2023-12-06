import json
import shapely
from shapely.wkt import loads
from shapely.geometry import mapping
import geojson
import matplotlib as plt

from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import shape

############################################################################################
# Convert geojson to shapely polygon
############################################################################################

from shapely.geometry import shape
from shapely.geometry.polygon import Polygon
'''  {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              28.4874173505483,
              41.56314098794968
            ],
            [
              28.3141785902844,
              40.67591663499303
            ],
            [
              32.93604091048252,
              39.78301389641658
            ],
            [
              32.90288633149217,
              40.40177040007765
            ],
            [
              28.4874173505483,
              41.56314098794968
            ]
          ]
        ],
        "type": "Polygon"
      }
    }
  ]
}'''

geo: dict = {'type': 'Polygon',
   'coordinates': [[[28.4874173505483, 41.56314098794968],
   [28.3141785902844, 40.67591663499303],
   [32.93604091048252, 39.78301389641658],
   [32.90288633149217, 40.40177040007765],
   [28.4874173505483, 41.56314098794968]]]}

Polygon = shape(geo)
print(Polygon)




############################################################################################
# Convert GeoJSON geometry to new coordinate system and WKB format in python
# Maslak-METU Devrim(:
############################################################################################

''' {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            29.02193919468337,
            41.10998965122576
          ],
          [
            32.785344503851405,
            39.89149481022565
          ]
        ],
        "type": "LineString"
      }
    }
  ]
}
'''

import json
import shapely
from shapely import wkb, wkt
from shapely.geometry import LineString

# Opening JSON file
f = open('Queries/istank.geojson')
data = json.load(f)

for i in data["features"]:
   geom = LineString(i['geometry']['coordinates'])

   g = wkb.dumps(geom, hex=True, srid=3857)

print(g)


############################################################################################
# Shapely coordinate sequence to GeoDataFrame
############################################################################################
'''
- Make a shapely polygon geometry from coordinate pairs
- Pass the polygon to GeoDataFrame constructor as a list
'''
import geopandas as gpd
from shapely.geometry import Polygon

coords = [(28.4874173505483, 41.56314098794968),
          (28.3141785902844, 40.67591663499303),
          (32.93604091048252, 39.78301389641658),
          (32.90288633149217, 40.40177040007765),
          (28.4874173505483, 41.56314098794968)]

polygon = Polygon(coords)

gdf = gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[polygon])
print(gdf)

