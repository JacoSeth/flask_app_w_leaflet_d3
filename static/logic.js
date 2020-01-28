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
  onEachFeature: function (feature, layer) {
    layer.on({
      mouseover: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function (event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup(function () {
      return "<hr> <h2>" + feature.properties.county + " COUNTY" + "</h2> <hr> <h3>" + "Population: " + feature.properties.pop_2010 + "</h3>"
    })
  }
});


var totalSubscribers = [];
var totalMembers = [];
var totalUnverified = [];
var totalNonMembers = [];

var congressionalGeoLayer = new L.GeoJSON(stateCongressionalDistricts, {
  style: mapStyleTwo,
  onEachFeature: function (feature, layer) {
    // var totalSubscribers = [];
    // var totalMembers = [];
    // var totalUnverified = [];
    // var totalNonMembers = []
    layer.on({
      mouseover: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function (event) {
        d3.json(`/cd_${feature.properties.FID}`, function (countData) {
          for (var i = 0; i < countData.length; i++) {
            console.log(countData);
            // create a reference variable for each object
            var count = countData[i];
            var totalSubs = count.x_district_subscribers_count;
            var totalMems = count.x_district_total_members;
            var totalUnverifieds = count.xd_uv_count;
            var totalNonMems = count.xd_nm_total;
            // interesting choice; why do you keep adding the users' choice to a list (totalSubscribers)
            // instead of just saving their choice itself (totalSubs)
            // do you want to track users' click history?
            totalSubscribers.push(totalSubs);
            totalMembers.push(totalMems);
            totalUnverified.push(totalUnverifieds);
            totalNonMembers.push(totalNonMems)
            
            // following this approach:
            // https://github.com/Leaflet/Leaflet/issues/947#issuecomment-118051406
            popup = event.target.getPopup()
            popup.setContent("<hr> <h2>"
            + "Congressional District "
            + feature.properties.FID
            + "</h2> <hr> <h2>" + "Total Subscribers :"
            + totalSubscribers[totalSubscribers.length - 1]
            + "</h2>");
            popup.update();
            // paranoid : make sure it's open (bindPopup() should do that)
            popup.openOn(map);
          }
        })
        // map.fitBounds(event.target.getBounds())
      },
    });
    // let's start with generic text:... see above code *after the d3 cd_ data is fetched*
    // which will update the popup content with subscribers count...
    layer.bindPopup("<hr> <h2>"
    + "Congressional District "
    + feature.properties.FID
    + "</h2>");
    // function () {
    //   return "<hr> <h2>"
    //     + "Congressional District "
    //     + feature.properties.FID
    //     + "</h2> <hr> <h2>" + "Total Subscribers :"
    //     + totalSubscribers[totalSubscribers.length - 1]
    //     + "</h2>"
    // })
  }
});

var stateHouseGeoLayer = new L.GeoJSON(stateHouseDistricts, {
  style: mapStyleTwo,
  onEachFeature: function (feature, layer) {
    layer.on({
      mouseover: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function (event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup(function () {
      return "<hr> <h2>" + "State House District " + feature.properties.FID + "</h2> <hr>"
    })
  }
});

var stateSenateGeoLayer = new L.GeoJSON(stateSenateDistricts, {
  style: mapStyleTwo,
  onEachFeature: function (feature, layer) {
    layer.on({
      mouseover: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#2f4754",
          fillOpacity: 0.7
        });
      },
      mouseout: function (event) {
        layer = event.target;
        layer.setStyle({
          fillColor: "#be1e2e",
          fillOpacity: 0.45
        });
      },
      click: function (event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    layer.bindPopup(function () {
      return "<hr> <h2>" + "State Senate District " + feature.properties.FID + "</h2> <hr>"
    })
  }
});

// Marker object
var userMarkers = [];

// User Icon
var userIcon = L.icon({
  iconUrl: 'static/CaucusRoomUserMarker.png',
  iconSize: [16, 16], // size of the icon
  iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
  // popupAnchor:  [0, -20] // point from which the popup should open relative to the iconAnchor
});

// User Layer object
var userLayer = L.layerGroup();

// Function to call geocoordinates into users object

d3.json('/user_data', function (userData) {
  for (var i = 0; i < userData.length; i++) {
    // create a reference variable for each object
    var user = userData[i];
    if (
      user.latitude && user.longitude
    ) {
      userMarkers.push(
        L.marker([user.latitude, user.longitude], { icon: userIcon })
          .bindPopup(function () {
            return '<h5>' + 'Role: ' + user.roles + '</h5>' + '<h5>' + 'County: ' + user.county + '</h5>' + '<h5>' + 'Congressional District: ' + user.cd + '</h5>' + '<h5>' + 'State Senate District: ' + user.sd + '</h5>' + '<h5>' + 'State House District: ' + user.hd + '</h5>'
          })
          .addTo(userLayer))
      // userLayer = L.layerGroup(userMarkers);
    }
  }
});


// baseMap & overlayMap
var baseMaps = {
  "Light": lightMap,
  // "Dark": darkMap,
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
  layers: [streetMap, congressionalGeoLayer, userLayer]
});

L.control.layers(baseMaps, overlayMaps).addTo(map);

