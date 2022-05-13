let currentCenterMarker;
function drawCenterMarker(map){
    currentCenterMarker = drawNewMarker(map, map.getCenter().x, map.getCenter().y);
}

function getCsrfToken(){
    return document.cookie.split(";")
        .find((item) => item.includes("csrftoken"))
        .split("=")[1];
}
