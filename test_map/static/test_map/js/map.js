let map = null;
let zoom = 15;
window.onload = onLoadActions;

function onLoadActions() {
    drawMap();
}

function drawMap(){
    let mapOptions = {
        center: new naver.maps.LatLng(37.3595704, 127.105399),
        zoom: zoom,
        zoomControl: true,
    };
    
    map = new naver.maps.Map('map', mapOptions);
}
