function panWest(){
    let width = document.getElementById("map").offsetWidth;
    map.panBy(new naver.maps.Point(-width, 0));
}

function panEast(){
    let width = document.getElementById("map").offsetWidth;
    map.panBy(new naver.maps.Point(width, 0));
}

function panNorth(){
    let height = document.getElementById("map").offsetHeight;
    map.panBy(new naver.maps.Point(0, -height));
}

function panSouth(){
    let height = document.getElementById("map").offsetHeight;
    map.panBy(new naver.maps.Point(0, height));
}

function zoomOut(){
    if (!(zoom > 5)) {
        return;
    }
    map.setZoom(--zoom);
}

function zoomIn(){
    if (!(zoom < 21)) {
        return;
    }
    map.setZoom(++zoom);
}

function zoomMax(){
    zoom = 21;
    map.setZoom(zoom, true);
}

function zoomMin(){
    zoom = 5;
    map.setZoom(zoom, true);
}

function setCenter(lat, long){
    map.setCenter(new naver.maps.Point(lat, long));
}

function drawNewMarker(map, lat, long){
    return new naver.maps.Marker({
        map: map,
        position: new naver.maps.Point(lat, long),
        zIndex: 100
    });
}

function showMarker(map, marker) {
    if(marker.getMap()) return;
    marker.setMap(map);
}

function hideMarker(marker) {
    if(!marker.getMap()) return;
    marker.setMap(null);
}

const defaultInfoElement = "Hello World!";
function addInfoWindowToMarker(marker, infoElement) {
    let infoWindow = new naver.maps.InfoWindow({
        content: infoElement ? infoElement : defaultInfoElement,
        marker: marker,
        zIndex: 150,
    });
    infoWindowDefaultListener(marker, infoWindow);
}

function infoWindowDefaultListener(marker, infoWindow){
    console.log(marker);
    naver.maps.Event.addListener(marker, "click", (e) => {
        if (infoWindow.getMap()) {
            infoWindow.close();
        } else {
            infoWindow.open(map, marker);
        }
    });
}
