let map = null;
window.onload = onLoadActions;

function onLoadActions() {
    drawMap();
}

function drawMap(){
    let mapOptions = {
        center: new naver.maps.LatLng(37.3595704, 127.105399),
        zoom: 15,
        zoomControl: true,
    };
    
    map = new naver.maps.Map('map', mapOptions);
}

function panWest(){
    let width = document.getElementById("map").offsetWidth;
    map.panBy(new naver.maps.Point(-width, 0));
}
function panEast(){
    let width = document.getElementById("map").offsetWidth;
    map.panBy(new naver.maps.Point(width, 0));
}

function zoomMax(){
    map.setZoom(21, true);
}

function zoomMin(){
    map.setZoom(5, true);
}

function setCenter(lat, long){
    map.setCenter(new naver.maps.Point(lat, long));
}

function drawNewMarker(map){
    new naver.maps.Marker({
        map: map,
        position: new naver.maps.LatLng(37.3595704, 127.105399),
        zIndex: 100
    });
}
