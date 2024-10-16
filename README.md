# simple-network
Applied network simplification

Proof of concept of network simplification using [sgeop](https://github.com/uscuni/sgeop) python package in a dockerized environment.

To be used as a development image in VS Code; the image is based on Ubuntu 24.04 and includes necessary packages for building and running the sgeop package.

## Usage
- */R* directory contains single file to create geopackage of a road network from OSM - it doesn't really matter which city you choose, but Plzeň is a good starting point :beers:.
- */python* directory contains a simple script to simplify the network; this is the action! The file should be executed from within the DevContainer in VS Code.
- */data* directory contains the input and output files for the network simplification; these are gitignored for the sake of repo size, but can be generated using the /R and /python scripts.
- _visual-overview.qgz_ is a QGIS project file to validate the results visually