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
        clickedMarkers.push(drawNewMarker(map, e.coord.x, e.coord.y));
    });
}

function reset(){
    clickedMarkers.forEach(marker => {
        hideMarker(marker);
    });
    clickedMarkers.splice(0, clickedMarkers.length);
    clickedMarkers.length = 0;
}

function sendSelectedPointsToServer(){
    let payload = {
        points: []
    }
    clickedMarkers.forEach(marker => {
        let point = {
            lat: marker.getPosition().x,
            long: marker.getPosition().y,
        }
        payload.points.push(point);
    });

    fetch("/map/save-points/", {
        method: "post",
        headers: {
            "X-CSRFToken": getCsrfToken(),
        },
        body: JSON.stringify(payload),
    }).then(response => {
        if(response.status != 200){
            alert("저장에 실패 했습니다!");
        } else {
            alert("저장에 성공 했습니다!");
        }
    });
}

function getPoints(){
    fetch("/map/get-points/")
        .then(response => {
            if (response.status == 200){
                response.json().then((responseBody) => drawPoints(responseBody.points));
            }
        });
}

function drawPoints(pointList){
    console.log(pointList);
    pointList.forEach(point => {
        console.log(point.lat);
        console.log(drawNewMarker(map, point.lat, point.long));
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
