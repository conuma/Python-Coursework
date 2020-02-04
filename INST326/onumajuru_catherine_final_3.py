import pickle
fh = open('onumajuru_catherine_latlon.txt', 'rb')
latlon = pickle.load(fh)
coord_list = []
fh_coord = open('onumajuru_catherine.js', 'w')
fh_coord.write('var addressPoints = [')
for i in latlon:
    coord_split = i.split(':')
    coord = coord_split[0]
    coord_list.append(coord)
    fh_coord.write('['+coord+'], ')
fh_coord.write('];')
fh_coord.close()

f = open('onumajuru_catherine.html','w')
block = """<html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src="onumajuru_catherine.js"></script>

    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24';
        var baseLayer = L.mapquest.tileLayer('map');

        var map = L.mapquest.map('map', {
          center: [0, 0],
          layers: baseLayer,
          zoom: 2
        });

        addressPoints = addressPoints.map(function (addressPoint) { return [addressPoint[0], addressPoint[1]]; });

        L.heatLayer(addressPoints).addTo(map);
      }
    </script>
  </head>

  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>"""
f.write(block)
f.close()
