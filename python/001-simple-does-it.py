import sgeop
import geopandas as gpd
import datetime as dt

# hláška pro diváky
print(F'{dt.datetime.now()} načítám data')

# Load the data
gdf = gpd.read_file("./data/raw-pilsen.gpkg")

# hláška pro diváky
print(F'{dt.datetime.now()} načteno, zjednodušuji...')

simplified = sgeop.simplify_network(gdf)

# hláška pro diváky
print(F'{dt.datetime.now()} zjednodušeno, ukládám...')

gdf.to_file("./data/clean-pilsen.gpkg")

# hláška pro diváky
print(F'{dt.datetime.now()} uloženo, all clear!')
