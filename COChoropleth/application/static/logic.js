// Insert csv path
var csv = ('/Users/sethjacobson/Desktop/COChoropleth/data/CR-admin-export_1.16.2020.csv')

// Map layers

var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  })

var darkMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
})

var streetMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
})

// geoMap styles
var mapStyle = {
    color: "#be1e2e",
    fillColor: "#2f4754",
    fillOpacity: 0.45,
    weight: 1.5
  };

var mapStyleTwo = {
    color: "#2f4754",
    fillColor: "#be1e2e",
    fillOpacity: 0.45,
    weight: 1.5
  };

// Geo layers 
var countyGeoLayer = new L.GeoJSON(countyGeoData, {
  style: mapStyleTwo,
  onEachFeature: function(feature, layer) {
    layer.on({
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function(event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup("<hr> <h2>" + feature.properties.county +" COUNTY" + "</h2> <hr> <h3>" + "Population: " + feature.properties.pop_2010 + "</h3>")
  }
});   

var congressionalGeoLayer = new L.GeoJSON(stateCongressionalDistricts, {
  style: mapStyleTwo,
  onEachFeature: function(feature, layer) {
    layer.on({
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function(event) {
        d3.json(`/cd_${feature.properties.FID}`, function(counts) {
          console.log(counts)
          // counts.forEach((sample) => {
          //     selector
          //         .append("option")
          //         .text(sample)
          //         .property("value", sample);
      
          })
        map.fitBounds(event.target.getBounds())
      },
    }),
    layer.bindPopup("<hr> <h2>" + "Congressional District " + feature.properties.FID + "</h2> <hr>")
  }
});

var stateHouseGeoLayer = new L.GeoJSON(stateHouseDistricts, {
  style: mapStyleTwo,
  onEachFeature: function(feature, layer) {
    layer.on({
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function(event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup("<hr> <h2>" + "State House District " + feature.properties.FID + "</h2> <hr>")
  }
});

var stateSenateGeoLayer = new L.GeoJSON(stateSenateDistricts, {
  style: mapStyleTwo,
  onEachFeature: function(feature, layer) {
    layer.on({
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function(event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function(event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup("<hr> <h2>" + "State Senate District " + feature.properties.FID + "</h2> <hr>")
  }
});

// Marker object
var userMarkers= [];

// User Icon
var userIcon = L.icon({
  iconUrl: 'resources/CaucusRoomUserMarker.png',
  iconSize: [16,16], // size of the icon
  iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
  // popupAnchor:  [0, -20] // point from which the popup should open relative to the iconAnchor
});

// User Layer object
var userLayer = L.layerGroup();

// Function to call geocoordinates into users object

d3.csv(csv, function(userData){
  for (var i = 0; i < userData.length; i++) {
    // create a reference variable for each object
    var user = userData[i];
    if (
      user.latitude && user.longitude
    ){
      userMarkers.push(
          L.marker([user.latitude, user.longitude], { icon: userIcon})
          .bindPopup('<p>' + 'Name: ' + user.firstName + ' ' + user.lastName + '</p>' + '<hr>' + '<p>' + 'City: ' + user.city + '</p>' + '<hr>' + '<p>' + 'County: ' + user.county + '</p>' + '<hr>' + '<p>' + 'Roles: ' + user.roles + '</p>')
          .addTo(userLayer))
        // userLayer = L.layerGroup(userMarkers);
}}});


// baseMap & overlayMap
var baseMaps = {
  "Light": lightMap,
  "Dark": darkMap,
  "Streets": streetMap
}

var overlayMaps = {
  "Counties": countyGeoLayer,
  "Congressional Districts": congressionalGeoLayer,
  "State House Districts": stateHouseGeoLayer,
  "State Senate Districts": stateSenateGeoLayer,
  "Users": userLayer
}

// Call map
var map = L.map("map", {
  center: colorado,
  zoom: 7,
  maxZoom: 18,
  minZoom: 1,
  layers:[streetMap, countyGeoLayer, userLayer]
});

L.control.layers(baseMaps, overlayMaps).addTo(map);

