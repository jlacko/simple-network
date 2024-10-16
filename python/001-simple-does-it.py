import sgeop
import geopandas as gpd
import datetime as dt



# hláška pro diváky
log = open('log.txt', 'w')
log.writelines(F'{dt.datetime.now()} načítám data\n')
log.close()

# Load the data
gdf = gpd.read_file("./data/raw-pilsen.gpkg")

# hláška pro diváky
log = open('log.txt', 'a')
log.writelines(F'{dt.datetime.now()} načteno, zjednodušuji...\n')
log.close()

# zde budiž akce! co se argumentů týče spolehneme na defaulty
simplified = sgeop.simplify_network(gdf)

# hláška pro diváky
log = open('log.txt', 'a')
log.writelines(F'{dt.datetime.now()} zjednodušeno, ukládám...\n')
log.close()

# Save the data
simplified.to_file("./data/clean-pilsen.gpkg")

# hláška pro diváky
log = open('log.txt', 'a')
log.writelines(F'{dt.datetime.now()} uloženo, all clear!')
log.close()
