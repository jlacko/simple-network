library(osmdata)
library(sf)

# hláška pro diváky
cat(paste(Sys.time(), "Začínám stahovat data z OSM...\n"))

# stejně dobrý město jako každý jiný...
result <- opq("Plzeň") %>%
    add_osm_feature(key = "highway",
                    value = c("motorway", "trunk", "primary", "secondary",
                              "tertiary", "housing", "residential")) %>%
    osmdata_sf()

# pouze čáry
ulice <- result$osm_lines %>%
    dplyr::select(name) %>%
    st_transform(5514) # jeden Křovák vládne všem!

# hláška pro diváky
cat(paste(Sys.time(), "data stažena, ukládám\n"))

# uložit pro budoucí použití - arrow by byl více frajerský, ale geopackage je rock solid
st_write(ulice, "./data/raw-pilsen.gpkg", delete_dsn = TRUE)

# hláška pro diváky
cat(paste(Sys.time(), "data uložena; all clear!\n"))