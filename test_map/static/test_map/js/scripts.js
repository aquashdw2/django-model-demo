let currentCenterMarker;
let currentInfoWindow;
function drawCenterMarker(map){
    if (currentCenterMarker) hideMarker(currentCenterMarker);
    if (currentInfoWindow) currentInfoWindow.close();
    currentCenterMarker = drawNewMarker(map, map.getCenter().x, map.getCenter().y);
    currentInfoWindow = addInfoWindowToMarker(
        currentCenterMarker,
        `<div class="info-window">Last Center: ${map.getCenter().x}, ${map.getCenter().y}</div>`
    );
}

let clickedMarkers = [];
function addMapClickEvent(){
    naver.maps.Event.addListener(map, "click", (e) => {
        console.log(e.coord);
        drawNewMarker(map, e.coord.x, e.coord.y);
    });
}


function findInCookie(cookieName){
    return document.cookie.split(";")
        .find((item) => item.includes(cookieName))
        .split("=")[1];
}

function getCsrfToken(){
    return findInCookie("csrftoken")
}
