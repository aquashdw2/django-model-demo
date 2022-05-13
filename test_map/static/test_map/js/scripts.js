let currentCenterMarker;
function drawCenterMarker(map){
    currentCenterMarker = drawNewMarker(map, map.getCenter().x, map.getCenter().y);
}

function findInCookie(cookieName){
    return document.cookie.split(";")
        .find((item) => item.includes(cookieName))
        .split("=")[1];
}

function getCsrfToken(){
    return findInCookie("csrftoken")
}
